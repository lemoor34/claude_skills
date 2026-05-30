#!/usr/bin/env python3
"""
Генератор og:image для fleissig-reinigung.ch через fal.ai (FLUX)
Запуск: python generate-og-image.py
Результат: og-image.png (1200x630px) — загрузить в /public/ сайта
"""

import fal_client
import requests
import os

FAL_KEY = "02a8065b-07d6-4770-a62c-5cc31f3a5593:c54dbe1b7da29a01e65ca6133f3abc50"
os.environ["FAL_KEY"] = FAL_KEY

PROMPT = (
    "Professional cleaning company logo banner, Swiss style, clean modern design. "
    "Dark green background (#3D7B4F), white text 'Fleissig' large and bold, "
    "subtitle 'Reinigung & Gartenpflege · Kanton Aargau', "
    "small icons: sparkle/clean, leaf/garden. "
    "Minimalist, premium, trustworthy. No people, no photos. "
    "Wide banner format 1200x630 pixels."
)

def main():
    print("Генерирую og:image через fal.ai FLUX...")

    result = fal_client.run(
        "fal-ai/flux/schnell",
        arguments={
            "prompt": PROMPT,
            "image_size": {"width": 1200, "height": 630},
            "num_inference_steps": 4,
            "num_images": 1,
            "enable_safety_checker": True,
        },
    )

    image_url = result["images"][0]["url"]
    print(f"Изображение готово: {image_url}")

    print("Скачиваю...")
    response = requests.get(image_url)
    with open("og-image.png", "wb") as f:
        f.write(response.content)

    print("✅ Сохранено: og-image.png")
    print("➡️  Загрузи файл в папку /public/ твоего React-проекта")
    print("➡️  Убедись что он доступен по: https://fleissig-reinigung.ch/og-image.png")

if __name__ == "__main__":
    main()
