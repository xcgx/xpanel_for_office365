# xpanel_for_office365

A third-party contral panel based on Python and SQL for office365.

# ****To Do List****

- [ ]  Auto transform all formed txt to UTF-8 txt then to csv.
- [ ]  Import accounts and passwords from csv(separate with',' or ':') to a sql.
- [ ]  Try to log in with ****[Azure CLI](https://github.com/Azure/azure-cli)****.
- [ ]  Try to log in with **[Office 365 CLI](https://github.com/pnp/cli-microsoft365).**
- [ ]  Try to log in with [**WEB**](https://portal.office.com).
- [ ]  Log all loging logs and time and status even screenshots
- [ ]  Try to figure out automaticlly whether user admin/global admin/bill admin/normal user
- [ ]  Automaticlly get subscribe on this tenant.
- [ ]  Automaticlly get apis if it’s global admin.
- [ ]  Try alias function and recieve emails.
- [ ]  Automaticlly judge whether this account/tenant is forgotten.
- [ ]  Push good result to tg.
- [ ]  Web_ui.
- [ ]  Proxy.
- [ ]  One_key output profile with excel to **[o365](https://github.com/vanyouseea/o365).**
- [ ]  Lookup azure panel and subs.

# ****Third Party Libs****

chardet sqlalchemy

# ****Known bugs****

empty txt/csv will crash file_initialization.py