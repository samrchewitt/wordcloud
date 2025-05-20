# import external libs 
import os
from os import path
from PIL import Image
from wordcloud import WordCloud

# Import stopwords with nltk.
from nltk.corpus import stopwords
stop = stopwords.words('english')

# import local 
from config import space_text, list_text, data_dir, pastel_palette, image_res
from utils.prepare import import_data
from utils.filters import filter_text
from services.createImages import invert_mask, SimpleGroupedColor

# import data from data directory
df = import_data(data_dir)

# filter in rows 
df_f = filter_text(df, 'Space Name', space_text, method='in')

# filter out rows 
df = filter_text(df_f, 'List Name', list_text, method='out')

# exclude stop words with list comprehension
df['Task Name'] = df['Task Name'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
# Drop NaN values from 'Task Content' column
df = df.dropna(subset=['Task Content'])

# Then apply the stopword removal
df['Task Content'] = df['Task Content'].apply(
    lambda x: ' '.join([word for word in x.split() if word not in stop])
)

# concatenate all the text in the Task Name and Task Content columns as task 
task = ' '.join(df['Task Name'].astype(str) + ' ' + df['Task Content'].astype(str))

print(f"Task: {task}")

# Generate a word cloud image from asset
mask = invert_mask("./assets/original_DCP.jpg")
wordcloud_DCP = WordCloud(background_color="white", mode="RGBA", max_words=5000, 
                          mask=mask,color_func=SimpleGroupedColor(pastel_palette),
                            width=image_res[0], height=image_res[1], # high-res width/height
                            ).generate(task)
# save wordcloud image to ouput folder
if not os.path.exists('output'):
    os.makedirs('output')
# save
wordcloud_DCP.to_file(path.join('output', 'wordcloud_DCP.png'))

# blend back in the original image 
# Generate word cloud as RGBA image
wc_image = wordcloud_DCP.to_image().convert("RGBA")
wc_size = wc_image.size  # (width, height)

# Load original background image
original_bg = Image.open("./assets/original_DCP.jpg").convert("RGBA")
original_bg = original_bg.resize(wc_size, Image.Resampling.LANCZOS)

# Blend word cloud with original background (adjust alpha as needed)
blended = Image.blend(original_bg, wc_image, alpha=0.7)  # 70% wordcloud

# Save blended result
blended.save(path.join('output', 'wordcloud_DCP_blended_v2.png'))