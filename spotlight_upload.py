import os
from supabase import create_client, Client
from timeit import default_timer as timer

SUPABASE_URL="https://xxzqhkwcmsvxgmqznltv.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inh4enFoa3djbXN2eGdtcXpubHR2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2NTE5NTU3MjgsImV4cCI6MTk2NzUzMTcyOH0.ocb6VJzB4IzksCssblMO4AAUfKHntkRn55c1STIq7pY"

url: str = SUPABASE_URL
key: str = SUPABASE_KEY
supabase: Client = create_client(url, key)

path = os.path.expanduser('~\Pictures\Spotlight Collection')
print(path)

start = timer()
for file in os.listdir(path):
    filename = os.fsdecode(file)
    
    try:
        print(os.path.join(path, filename))
        supabase.storage().from_('spotlight-photos').upload('public/%s' % (filename), os.path.join(path, filename), { 'content-type': 'image/jpeg' })
        image_url = supabase.storage().from_('spotlight-photos').get_public_url('public/%s' % filename)
        supabase.table("spotlight_photos").insert({ "id": filename, "url": image_url }).execute()
        print('OK')
    except Exception as e: 
        print('Error: %s' % e)

end = timer()
ellapsed = end - start

print('DONE in %ss' % (ellapsed))