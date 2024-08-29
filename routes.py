from flask import render_template, redirect, url_for, flash
from models import db, Transaction
from forms import TransactionForm
from datetime import datetime

def init_routes(app):
    
    @app.route('/')
    def index():
        transactions = Transaction.query.all()
        return render_template('index.html', transactions=transactions)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = TransactionForm()
        if form.validate_on_submit():
            transaction = Transaction(
                date=form.date.data,
                description=form.description.data,
                amount=form.amount.data,
                type=form.type.data
            )
            db.session.add(transaction)
            db.session.commit()
            flash('Transaction added successfully!', 'success')
            return redirect(url_for('index'))
        return render_template('register.html', form=form)

    @app.route('/report')
    def report():
        incomes = db.session.query(Transaction).filter_by(type='income').all()
        expenses = db.session.query(Transaction).filter_by(type='expense').all()
        total_income = sum([t.amount for t in incomes])
        total_expense = sum([t.amount for t in expenses])
        balance = total_income - total_expense
        return render_template('report.html', total_income=total_income, total_expense=total_expense, balance=balance)
