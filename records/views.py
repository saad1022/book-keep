from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView ,DeleteView
from .models import Entry
from .forms import EntryForm
from django.urls import reverse_lazy
from django.db.models import Sum , Avg
from datetime import datetime


currentMonth = datetime.now().month
currentYear = datetime.now().year

entry_data = list(Entry.objects.filter(account='Income').aggregate(Sum('amount')).values())[0]
exp_data = list(Entry.objects.exclude(account='Income').aggregate(Sum('amount')).values())[0]

q_month_expenses = list(Entry.objects.filter(date_created__year=currentYear).filter(date_created__month=currentMonth).exclude(account='Income').aggregate(Sum('amount')).values())[0]
q_month_income = list(Entry.objects.filter(date_created__year=currentYear).filter(date_created__month=currentMonth).filter(account='Income').aggregate(Sum('amount')).values())[0]

q_year_expenses = list(Entry.objects.filter(date_created__year=currentYear).exclude(account='Income').aggregate(Sum('amount')).values())[0]
q_year_income = list(Entry.objects.filter(date_created__year=currentYear).filter(account='Income').aggregate(Sum('amount')).values())[0]

q_current_blnc = q_year_income - q_year_expenses

q_saad_income_month = list(Entry.objects.filter(date_created__year=currentYear).filter(date_created__month=currentMonth).filter(account='Income').filter(head='Saad').aggregate(Sum('amount')).values())[0]
q_saad_expense_month = list(Entry.objects.filter(date_created__year=currentYear).filter(date_created__month=currentMonth).exclude(account='Income').filter(head='Saad').aggregate(Sum('amount')).values())[0]

q_home_income_month = list(Entry.objects.filter(date_created__year=currentYear).filter(date_created__month=currentMonth).filter(account='Income').filter(head='Home').aggregate(Sum('amount')).values())[0]
q_home_expense_month = list(Entry.objects.filter(date_created__year=currentYear).filter(date_created__month=currentMonth).exclude(account='Income').filter(head='Home').aggregate(Sum('amount')).values())[0]

q_saad_blnc = q_saad_income_month - q_saad_expense_month
q_home_blnc = q_home_income_month - q_home_expense_month

# Create your views here.

class DashboardView(ListView):
	model = Entry
	template_name = 'dashboard.html'
	extrainfo = entry_data
	expenses = exp_data
	month_expenses = q_month_expenses
	month_income = q_month_income
	year_expense = q_year_expenses
	year_income = q_year_income
	current_balance = q_current_blnc
	saad_balance = q_saad_blnc
	home_balance = q_home_blnc

	def get_context_data(self, **kwargs):
		context =  super(DashboardView, self).get_context_data(**kwargs)
		context['extrainfo'] = self.extrainfo
		context['expenses'] = self.expenses
		context['month_expenses'] = self.month_expenses
		context['month_income'] = self.month_income
		context['year_income'] = self.year_income
		context['year_expense'] = self.year_expense
		context['current_balance'] = self.current_balance
		context['saad_balance'] = self.saad_balance
		context['home_balance'] = self.home_balance

		return context


class HomeView(ListView):
	model = Entry
	template_name = 'home.html'
	ordering = ['-date_created']
	
	#paginate_by = 10

class EntryDetailView(DetailView):
	model = Entry
	template_name = 'entry_detail.html'

class AddEntryView(CreateView):
	model = Entry
	form_class = EntryForm
	template_name = 'add_entry.html'

class UpdateEntryView(UpdateView):
	model = Entry
	form_class = EntryForm
	template_name = 'edit_entry.html'
	#fields = ['title' , 'body']


class DeleteEntryView(DeleteView):
	model = Entry
	template_name = 'del_entry.html'	
	success_url = reverse_lazy('home')