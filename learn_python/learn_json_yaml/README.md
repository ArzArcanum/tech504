# Comparing JSON and YAML

JSON:
```json
{
  "name": "John Doe",
  "age": 30,
  "isStudent": false,
  "courses": ["Python", "DevOps"],
  "address": {
    "street": "123 Main St",
    "city": "Anytown"
  }
}
```
* lists - uses []
* dictionaries - uses {}
* comma between items in lists + dict
* double quotes for keys & string values

YAML:
```yaml
name: John Doe
age: 30
isStudent: false
courses:
  - Python
  - DevOps
address:
  street: 123 Main St
  city: Anytown
```
* indenting is important
* lists - starting with hyphens
* strings - no quotes needed