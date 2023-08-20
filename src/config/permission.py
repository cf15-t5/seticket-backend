all_user_permission=[
  '/auth/me',
  '/auth/logout',
  '/categories',
  '/events/',
]

admin_permission=[
  '/auth/verify',
  '/users/',
  '/categories/*',
]

user_permission=[
]

event_organizer_permission=[
  '/events/*',
  '!/events/verify',

]
permissions = {
  'admin': admin_permission+all_user_permission,
  'user': user_permission+all_user_permission,
  'event_organizer': event_organizer_permission+all_user_permission,
}