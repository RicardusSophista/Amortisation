# Amortisation
A work in progress that will eventually allow the user to generate an amortisation schedule for a loan, with many different options for the repayment terms.

## Components
The amortisation schedule is generated and displayed by the `gen_amort` function. This takes the following parameters:
* `pr`: the principal, i.e., the amount borrowed
* `pmt`: the repayment amount. Currently this has to be a fixed amount. Allowing variable payments, e.g. x% of the outstanding balance, is on the todo list.
* `pmt_sched`: A list of `datetime` objects representing the dates when payments are due.
* `int_sched`: A list of `datetime` objects representing the dates when interest is capitalised. Optional parameter; if not specified, interest is assumed to capitalise on the repayment date.
* `int_only_sched`: Not currently functional. Will allow a schedule of interest-only repayments.

The Main function currently allows the user to specify basic rules for the loan schedule, i.e., the repayment frequency, capitalisation frequency, start and end dates, etc. These are then converted into lists of `datetime` objects that can be fed into the `gen_amort` function, using the `scheduler` module from this repository.

## Dependencies
Requires the `scheduler` module from this repository, as well as `datetime`.
