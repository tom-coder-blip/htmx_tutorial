from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt


#1) Update views.py to use index.html instead of example.html
def profile_view(request):
    return render(request, 'index.html')


#Step 2: Convert server.js Methods to Django Views
#Handle the GET request for Editing Profile
#Replace the /user/:id/edit logic with a Django view.
def edit_profile(request, user_id):
    """Returns the profile edit form."""
    return HttpResponse(f'''
           <form hx-put="/user/{user_id}/" 
              hx-target="this" 
              hx-swap="outerHTML"
              class="p-3 border rounded">

            <div class="mb-3">
                <label for="name" class="form-label">Name</label>
                <input type="text" class="form-control" id="name" name="name" value="Greg Lim">
            </div>
            <div class="mb-3">
                <label for="bio" class="form-label">Bio</label>
                <textarea class="form-control" id="bio" name="bio">Follower of Christ | Author of Best-selling Amazon Tech Books and Creator of Coding Courses</textarea>
            </div>

            <button type="submit" class="btn btn-primary">Save Changes</button>
            <button type="button" hx-get="/user/1/edit/" hx-target="this" hx-swap="outerHTML" class="btn btn-secondary">Cancel</button>
        </form>
    ''')

#Handle the PUT Request for Saving Profile Updates
#Django doesn't support PUT requests directly with request.POST, so we need to allow it explicitly.
@csrf_exempt  # Disable CSRF for simplicity (not recommended for production)
def update_profile(request, user_id):
    """Handles profile updates."""
    if request.method == "PUT":
        put = QueryDict(request.body.decode('utf-8'))
        # Use request.POST instead of json.loads(request.body)
        name = put.get('name', 'Unknown')
        bio = put.get('bio', '')

        return HttpResponse(f'''
        <div class="card" style="width: 18rem;"
        hx-target="this"
        hx-swap="outerHTML"
        >
            <div class="card-body">
                <h5 class="card-title">{name}</h5>
                <p class="card-text">
                    {bio}
                </p>
                <button href="#" class="btn btn-primary"
                hx-get="/user/{user_id}/edit">
                    Click To Edit
                </button>
            </div>
        </div>
        ''')

    return HttpResponse("Invalid request", status=400)