month_conversion = {
    "Jan" : "January",
    2 : "February",
    "Mar" : "March",
    "April": "April",
    "May" : "May"
}

print(month_conversion[2])

print(month_conversion.get("Mar"))

print(month_conversion.get("Luv", "Not a valid key"))