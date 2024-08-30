from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from models import db, Transaction
from forms import TransactionForm

def init_routes(app):

    @app.route('/')
    @login_required
    def index():
        transactions = Transaction.query.filter_by(user_id=current_user.id).all()
        return render_template('index.html', transactions=transactions)

    @app.route('/transaction/create', methods=['GET', 'POST'])
    @login_required
    def create_transaction():
        form = TransactionForm()
        if form.validate_on_submit():
            transaction = Transaction(
                date=form.date.data,
                description=form.description.data,
                amount=form.amount.data,
                type=form.type.data,
                user_id=current_user.id
            )
            db.session.add(transaction)
            db.session.commit()
            flash('Transaction added successfully!', 'success')
            return redirect(url_for('index'))
        return render_template('transaction_create.html', form=form)

    @app.route('/transaction/edit/<int:id>', methods=['GET', 'POST'])
    @login_required
    def edit_transaction(id):
        transaction = Transaction.query.get_or_404(id)
        if transaction.user_id != current_user.id:
            flash('You do not have permission to edit this transaction.', 'danger')
            return redirect(url_for('index'))
        form = TransactionForm(obj=transaction)
        if form.validate_on_submit():
            transaction.date = form.date.data
            transaction.description = form.description.data
            transaction.amount = form.amount.data
            transaction.type = form.type.data
            db.session.commit()
            flash('Transaction updated successfully!', 'success')
            return redirect(url_for('index'))
        return render_template('transaction_edit.html', form=form)

    @app.route('/transaction/delete/<int:id>', methods=['POST'])
    @login_required
    def delete_transaction(id):
        transaction = Transaction.query.get_or_404(id)
        if transaction.user_id != current_user.id:
            flash('You do not have permission to delete this transaction.', 'danger')
            return redirect(url_for('index'))
        db.session.delete(transaction)
        db.session.commit()
        flash('Transaction deleted successfully!', 'success')
        return redirect(url_for('index'))

    @app.route('/transactions/report')
    @login_required
    def transaction_report():
        incomes = db.session.query(Transaction).filter_by(type='income', user_id=current_user.id).all()
        expenses = db.session.query(Transaction).filter_by(type='expense', user_id=current_user.id).all()
        total_income = sum([t.amount for t in incomes])
        total_expense = sum([t.amount for t in expenses])
        balance = total_income - total_expense
        return render_template('transaction_report.html', total_income=total_income, total_expense=total_expense, balance=balance)