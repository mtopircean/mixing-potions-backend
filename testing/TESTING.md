**Area**|**Test number**|**Test Perfomed**|**Result**|**Mark**|**Corretive measure**|**Updated result**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
Profile App|1|Access profiles urls|Profiles are accessible and listed as expected|Pass|n/a|n/a
Profile App|1.1|Access individual profile url|Profile is accessible and listed as expected|Pass|n/a|n/a
Profile App|1.2|Access innexistent profile url|Message of non-existing page is returned-404 Not Found|Pass|n/a|n/a
Profile App|1.3|Update own profile|User can update their own profile|Pass|n/a|n/a
Profile App|1.4|Update another users profile - as admin|Admin can update another users profile|Pass|n/a|n/a
Profile App|1.5|Update another users profile - as another user|User can`t update another users profile|Pass|n/a|n/a
Profile App|1.6|Delete a profile - logged out|User does not have the delete option|Pass|n/a|n/a
Profile App|1.7|Delete a profile - logged in as another user|User does not have the delete option|Pass|n/a|n/a
Profile App|1.8|Delete a profile of another user - logged in as admin|User does not have the delete option|Pass|n/a|n/a
Profile App|1.9|Delete own logged in user profile|User does not have the delete option|Pass|n/a|n/a
Products App|2|Access products urls|Products are not accessible to non-admin users, only admin.|Pass|n/a|n/a
Products App|2.1|Access individual product url|Products are not accessible to non-admin users, only admin.|Pass|n/a|n/a
Products App|2.2|Access innexistent product url|Products are not accessible to non-admin users, only admin.|Pass|n/a|n/a
Products App|2.3|Update a product - as admin|Admin can update a product|Pass|n/a|n/a
Products App|2.4|Delete a product - as admin|Admin can delete a product|Pass|n/a|n/a
Posts App|3|Access posts urls|Posts are accessible and listed as expected|Pass|n/a|n/a
Posts App|3.1|Access individual post url|Post is accessible and listed as expected|Pass|n/a|n/a
Posts App|3.2|Access innexistent post url|Message of non-existing page is returned - 404 page|Pass|n/a|n/a
Posts App|3.3|Update own post|User can update their own post|Pass|n/a|n/a
Posts App|3.4|Update another users post - as admin|Admin can update another users post|Pass|n/a|n/a
Posts App|3.5|Update another users post - as another user|User can`t update another users post - put method not accessible|Pass|n/a|n/a
Posts App|3.6|Create a post - logged in|User can create a post|Pass|n/a|n/a
Posts App|3.7|Create a post - not logged in|User can`t create a post|Pass|n/a|n/a
Posts App|3.8|Delete a post - logged out|User does not have the delete option|Pass|n/a|n/a
Posts App|3.9|Delete a post - logged in as another user|User does not have the delete option|Pass|n/a|n/a
Posts App|3.9.1|Delete a post of another user - logged in as admin|Admin can delete a post|Pass|n/a|n/a
Posts App|3.9.2|Delete own logged in user post|User can delete their own|Pass|n/a|n/a
Followers App|4.1|Access followers urls|Followers are accessible and listed as expected to logged in users|Pass|n/a|n/a
Followers App|4.2|Access individual followers url|Follower is accessible and listed as expected to logged in users owning the follow|Pass|n/a|n/a
Followers App|4.3|Access innexistent followers url|Message of non-existing follow is returned|Pass|n/a|n/a
Followers App|4.4|Follow a user - logged in|User can follow another user|Pass|n/a|n/a
Followers App|4.5|Follow a user - not logged in|User can`t follow another user|Pass|n/a|n/a
Followers App|4.6|Follow own user|User can`t follow their own user - 400 error|Pass|n/a|n/a
Followers App|4.7|Follow own user - as admin|User can`t follow their own user|Pass|n/a|n/a
Followers App|4.8|Access followers urls|Followers are not accessible to users not logged in|Pass|n/a|n/a
Followers App|4.9|Access individual followers url|Follow is not accessible to users not owning it|Pass|n/a|n/a
Followers App|4.91|Delete a follow - logged out|User does not see other users follows|Pass|n/a|n/a
Followers App|4.92|Delete a follow - logged in as another user|User does not see other users follows|Pass|n/a|n/a
Followers App|4.93|Delete a follow of another user - logged in as admin|Admin can delete a follow|Pass|n/a|n/a
Followers App|4.94|Delete own logged in user follows|User can delete their own|Pass|n/a|n/a
Comments App|5.1|Access comments urls|Comments are accessible and listed as expected|Pass|n/a|n/a
Comments App|5.2|Access individual comments url|Comment is accessible and listed as expected|Pass|n/a|n/a
Comments App|5.3|Access innexistent comments url|Message of non-existing comment is returned|Pass|n/a|n/a
Comments App|5.4|Comment a post - logged in|User can comment a post|Pass|n/a|n/a
Comments App|5.5|Comment a post - not logged in|User can`t comment a post - 404 error|Pass|n/a|n/a
Comments App|5.6|Comment own post|User can comment own post|Pass|n/a|n/a
Comments App|5.7|Comment own post - as admin|User can comment own post|Pass|n/a|n/a
Comments App|5.8|Comment another users post - as another user|User can comment another users post|Pass|n/a|n/a
Comments App|5.9|Delete a comment - logged out|User does not have the delete option|Pass|n/a|n/a
Comments App|5.91|Delete a comment - logged in as another user|User does not have the delete option|Pass|n/a|n/a
Comments App|5.92|Delete a comment of another user - logged in as admin|Admin can delete a comment|Pass|n/a|n/a
Comments App|5.93|Delete own logged in user comments|User can delete their own|Pass|n/a|n/a
Likes App|6.1|Access likes urls|Likes are accessible and listed as expected|Pass|n/a|n/a
Likes App|6.2|Access individual like url - logged in user|Like is accessible and listed as expected|Pass|n/a|n/a
Likes App|6.3|Access innexistent like url|Message of non-existing like is returned - 403 forbiden|Pass|n/a|n/a
Likes App|6.4|Like a post - logged in|User can like another users|Pass|n/a|n/a
Likes App|6.5|Like a post - not logged in|User can`t like a post|Pass|n/a|n/a
Likes App|6.6|Like own post|User can like own post|Pass|n/a|n/a
Likes App|6.7|Like own post - as admin|User can like own post|Pass|n/a|n/a
Likes App|6.8|Like another users post - as another user|User can like another users post|Pass|n/a|n/a
Likes App|6.9|Access individual like url - not logged in user|Like is not accessible to not logged in user-403 error|Pass|n/a|n/a
Likes App|6.91|Access individual like url - not like owner|Like is not accessible to non-owner - 403 error|Pass|n/a|n/a
Likes App|6.92|Delete a like - logged out|User does not have the delete option|Pass|n/a|n/a
Likes App|6.93|Delete a like - logged in as another user|User does not have the delete option|Pass|n/a|n/a
Likes App|6.94|Delete a like of another user - logged in as admin|Admin can delete a like|Pass|n/a|n/a
Likes App|6.95|Delete own logged in user likes|User can delete their own|Pass|n/a|n/a