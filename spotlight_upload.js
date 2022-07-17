const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

require('dotenv').config()
const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY)
// WIN PATH: 'C:/Users/Wiktor/Pictures/Spotlight Collection'; 
// MAC PATH: '/Users/flwn/Downloads/Spotlight Collection'
const path = 'C:/Users/Wiktor/Pictures/Spotlight Collection'; 

fs.readdir(path, (err, files) => {
    for(const filename of files) {
        console.log('File:', filename);
        fs.readFile(`${path}/${filename}`, async (err, fileData) => {
            if (err) {
              console.error(err);
              return;
            }

            const uploadData = await supabase.storage.from('spotlight-photos').upload(
                `public/${filename}`, 
                fileData,
                { 
                    contentType: "image/jpeg",
                    cacheControl: '3600',
                    upsert: false
                }
            )   
            console.log('upload', uploadData);
            const { data: { publicURL } } = supabase.storage.from('spotlight-photos').getPublicUrl(`public/${filename}`)
            console.log('publicURL', publicURL);
            console.log('inserting...');
            await supabase.from('spotlight_photos').insert([
                { "id": filename, "url": publicURL }
            ])
            console.log('[DONE]', filename)
        });
    };
});