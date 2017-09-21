from functools import wraps


# def permissions(permission_fn):
#   print('PERMISSIONS')

#   def permissions_decorator(fn):
#     print('PERMISSIONS_DECORATOR')
#     # [f for f in filter(lambda f: f.name.value != 'visibility', info.field_asts[0].selection_set.selections)]

#     @wraps(fn)
#     def func_wrapper(info, *args, **kwargs):
#       import ipdb; ipdb.set_trace()
#   return permissions_decorator


def permissions(permission_function):

  def wrapper(old_function):

    def new_function(self, info, *args, **kwargs):
      permission_function(info)
      return old_function(self, info, *args, **kwargs)

    return new_function

  return wrapper
