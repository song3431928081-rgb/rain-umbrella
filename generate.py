import json, subprocess, os

prompts = {
  'scene-street': 'Game background asset: Anime illustration style, warm cozy Japanese alley at night. A couple walking together under a glowing shop awning, holding hands. Warm orange lantern lights from small shops lining narrow street. Rainy pavement reflecting lights. Signs in Japanese like 付け書房 and 雨宿. Wet cobblestone ground. Centered composition with negative space on right. Warm golden lighting, vibrant colors, cinematic feel. 16:9 landscape format, no watermark, no text overlay.',
  'scene-bus-stop': 'Game background asset: Anime illustration style, warm cozy bus stop at night. A group of young kids waiting together at the bus stop, some holding small umbrellas. Warm yellow light from bus stop sign glowing on them. Wet pavement reflecting warm light. Dark trees in background. Empty street. Centered composition. Warm lighting, vibrant colors, 16:9 landscape format, no watermark, no text overlay.',
  'scene-bench': 'Game background asset: Anime illustration style, warm cozy park at night. An elderly couple sitting together on a wooden park bench under a glowing lamppost, sharing one umbrella. Wet pavement reflecting light. Dark tree silhouettes in background. Empty park. Centered composition. Warm lighting, vibrant colors, 16:9 landscape format, no watermark, no text overlay.',
  'scene-ending': 'Game background asset: Anime illustration style, beautiful clear sky scene after rain. A brilliant rainbow arches across blue sky with fluffy white clouds. A girl walking up stone stairs in foreground, holding a closed umbrella and carrying a small bag. Distant town rooftops in valley below. Warm golden sunlight. Uplifting hopeful mood. 16:9 landscape format, no watermark, no text overlay.'
}

size = 'landscape_4_3'
for name, prompt in prompts.items():
    path = f'/workspace/rain-umbrella/{name}'
    print(f'Generating {name}...')
