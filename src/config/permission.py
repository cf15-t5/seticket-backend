all_user_permission=[
  '/auth/me',
  '/auth/logout',
  '/categories',
  '/events/',
  '/tickets/',
  '/users/update-profile',
  '/users/topup',
  '/users/withdraw',

]

admin_permission=[
  '/auth/verify',
  '/users/',
  '/categories/*',
  '/events/verify',
]

user_permission=[
  
]

event_organizer_permission=[
  '/events/*',
  '!/events/verify',
  '/tickets/attend',

]
permissions = {
  'admin': admin_permission+all_user_permission,
  'user': user_permission+all_user_permission,
  'event_organizer': event_organizer_permission+all_user_permission,
}