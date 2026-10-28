# Purpose of this Folder

This folder should contain the scaffolded project files to get a student started on their project. This repo will be added to the Classroom for students to use, so please do not have any solutions in this folder.

# Reflection

Design patterns implemented:
- Singleton: implemented in the Balance class. It ensures that the application has a single instance that keeps track of the balance and transactions, keeping the state consistent.
- Adapter: implemented in the TransactionAdapter class. It allows the application to work with external transactions that do not fit the internal transaction format. 
- Observer: the observers are implemented through IBalanceObserver, PrintObserver, and LowBalanceAlertObserver. The Balance class was updated to have methods to add and remove observers, and to notify them when the balance changes. This makes it easy to allow different reactions to balance changes without having to modify the Balance class itself and add new obsewrvers in the future.
- Strategy: The current strategies (for income and expenses) were implemented using the TransactionStrategy interface. This separates the transaction logic from the Balance class, allowing for an easier addition of new transaction types.

# Addtional pattern: Strategy

I decided to implement this pattern into the project as it already had different ways to process a transaction depending on its category (income or expense). Initially, the Balance class decided what to do with an if statement, but now it only needs to call the apply method of the strategy class. This makes it easier to add new transaction types or change the logic behind one in the future without touching the Balance class.

# Challenges
- Having to adjust the code to fit the requirements defined by the tests (e.g. the transaction string) or to work with the existing code (e.g. adjusting the transaction adapter to have just what it needed to work with external transactions)
- Deciding on a new pattern to implement in the project and how to implement it taking into account the existing code.