# GraphQL challenge

Joe owns a celebrity fashion shop. That is, he sells clothes and accessories usually worn by celebrities. He wants an app that allows people to easily browse all items or items worn by a specific celebrity. Furthermore he wants basic e-commerce capabilities so that people can buy such items directly via the app.

## Entities and relationships

Each celebrity has a name and age.

Each piece of clothing or accessory has an ID, a name, a price tag (in USD), the remaining quantity and a list of celebrities who wear it. Here is an example:

```
{
  "id": "SW5ncmVkaWVudE5vZGU6MQ"
  "name": "Ray-Ban Wayfarer",
  "price": 199.99,
  "quantity": 12,
  "celebrities": [
    {
      "name": "Leonardo di Caprio",
      "age": 55
    }, {
      "name": "Benedict Cumberbacht",
      "age": 41
    }
  ]
}
```

Items also have a **private** string field `visibility` that indicates whether the item is visible to every user (`public`) or only authenticated users (`authenticatedUsersOnly`). The default is `public`.

When listing the item's celebrities the user might also want to see the items worn by that specific celebrity. In that case the payload should include the relevant information. Example:

```
{
  "id": "SW5ncmVkaWVudE5vZGU6MQ"
  "name": "Ray-Ban Wayfarer",
  "price": 199.99,
  "quantity": 12,
  "celebrities": [
    {
      "name": "Leonardo di Caprio",
      "age": 55,
      "items": [
        {
          "id": "SW5ncmVkaWVudE5vZGU6MQ"
          "name": "Ray-Ban Wayfarer",
          "price": 199.99,
        },
        {
          "id": "SW5ncmVkaWVudE5vZGU6MZ"
          "name": "H&M Blazer",
          "price": 50.00,
        },
        {
          "id": "SW5ncmVkaWVudE5vZGU6MA"
          "name": "Mickey Mouse shoes",
          "price": 12.99,
        }
      ]
    }
  ]
}
```


## Authentication and Authorization

Authentication is handled by Django. Only authenticated users are allowed to buy items. Some items are only visible to authenticated users as explained above. To avoid additional complexity **we will not use DRF capabilities** and will solely rely on authenticating via the admin panel.

Authorization must be explicitly coded within the resolvers, either within its body, as a decorator or by inheriting from the `Query` class and have a custom root query type.

## Purchase

Every time an item is purchased its quantity decreases by the amount that has been purchased.

Modeling purchases **is entirely up to you**. You might decide to model them as a simple one-off action (e.g. `purchaseItem`) or as a separate entity (e.g. `createPurchase` + `Purchase` type).

## Endpoints

- `listItems: [ItemType]!`
- `retrieveItem(id: String): ItemType`
- `purchaseItem(id: String): ?` (The return type depends on how you model your system)

## Bonus

- Hide a selection of fields (e.g. `visibility`) **only** if the user is not authenticated, in a declarative way. Example:

```python
@permissions(hideVisibilityIfNotAuthenticated)
def resolve_list_items(self, info):
  ...
```