# REST APIs
Representational State Transfer
Transfer of `resources`, usually in `JSON` format over `http`, but not necessarily.
Stateless is an important requirement.

- Prefer nouns over verbs to name resources.
- Pagination by `limit` and `offset` (also, `page_size` and `page_offset`)
- Filter, sorting, projection by `query params` in a `GET` request, like `v1/order?amount_lte=200&sort_by=order_date&fields=amount,customer,products`

- GET
- POST
- PUT
- PATCH
- DELETE
- OPTIONS - preflight verification request for POST
- HEAD
