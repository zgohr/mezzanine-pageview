## Mezzanine Page View

Limit viewable CMS pages by group.

To install, add ```mezzanine_pageview.middleware.PageViewMiddleware``` to your ```MIDDLEWARE_CLASSES``` and ```mezzanine_pageview``` to your ```INSTALLED_APPS``` somewhere above ```mezzanine.pages```. Finally, ```./manage.py syncdb```.

### What's going on

I needed the ability to limit the pages that any particular user can see. This application is a middleware to throw a 404 error if the logged user does not have access to a group required to view a particular page, and a templatetag as well as modified navigation templates so the links do not get displayed.

Mezzanine has a concept called [page processors](http://mezzanine.jupo.org/docs/content-architecture.html#page-processors) that performs something between middelware and context processors for custom ```Page``` models. Unfortunately you cannot currently use page processors on the generic ```Page``` model.
