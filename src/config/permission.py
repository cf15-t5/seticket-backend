all_user_permission=[
  '/auth/me',
  '/auth/logout',
]

admin_permission=[
  '/auth/verify',
  '/users'
  
]

user_permission=[
]

event_organizer_permission=[

]
permissions = {
  'admin': admin_permission+all_user_permission,
  'user': user_permission+all_user_permission,
  'event_organizer': event_organizer_permission+all_user_permission,
}