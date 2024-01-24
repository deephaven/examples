# Calendar

This folder contains a calendar file in XML format.

## Table of contents

`CompanyY_2024.calendar`: A calendar file for a hypothetical company, `Company Y`, in XML format.

## Calendar file

A calendar file can be used by Deephaven's calendar API to add a custom calendar to the list of available calendars. This calendar file is used in Deephaven's documentation to show how this can be done.

## Use a custom calendar

Here's an example of the documentation for using a custom calendar:

```python
from deephaven.calendar import add_calendar, calendar, calendar_names

add_calendar("https://media.githubusercontent.com/media/deephaven/examples/main/Calendar/CompanyY_2024.calendar")

print(calendar_names())

company_y_cal_2024 = calendar("CompanyY_2024")
```