# dynamic-inventory
Dummy Ansible dynamic inventory

This inventory files lookup in the yml files for ```hosts: <something>```

the resulting inventory will be:

```json
{
  "<something>": [
    "localhost"
  ]
}
```
