import requests
from threading import Thread
import time
import concurrent.futures
from PIL import Image, ImageFilter
import multiprocessing

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c',
    'https://images.unsplash.com/photo-1633531138911-1dffbaa8d65d'
]

start = time.perf_counter()

# multiprocessing with executor
# size = (1200, 1200)
#
#
# def img_names(img_urls):
#     for url in img_urls:
#         name_ = url.split('/')[3]
#         name = f'{name_}.jpg'
#         yield name
#
#
# def process_image(img_name):
#     img = Image.open(img_name)
#     img = img.filter(ImageFilter.GaussianBlur(15))
#     img.thumbnail(size)
#     img.save(f'processed/{img_name}')
#     print(f'{img_name} was processed...')
#
#
# if __name__ == '__main__':
#     start = time.perf_counter()
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         executor.map(process_image, img_names(img_urls))

# multiprocessing my the books
# size = (1200, 1200)
#
#
# def img_names(img_urls):
#     for url in img_urls:
#         name = url.split('/')[3]
#         name = f'{name}.jpg'
#         yield name
#
#
# def process_image(img_name):
#     img = Image.open(f'images/{img_name}')
#     img = img.filter(ImageFilter.GaussianBlur(15))
#     img.thumbnail(size)
#     img.save(f'doneStuff/{img_name}')
#     print(f'{img_name} was processed...')
#
#
# if __name__ == '__main__':
#     start = time.perf_counter()
#     processes = []
#     for name in img_names(img_urls):
#         p = multiprocessing.Process(target=process_image, args=(name, ))
#         p.start()
#         processes.append(p)
#
#     for process in processes:
#         process.join()


# Download Images quicker
# def download_images(url):
#     print("started")
#     img_bytes = requests.get(url).content
#     img_name = url.split('/')[3]
#     img_name = f'{img_name}.jpg'
#     with open(f'images/{img_name}', 'wb') as img_file:
#         img_file.write(img_bytes)
#         print(f'{img_name} was downloaded...')
#
#
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     executor.map(download_images, img_urls)

# Loop concurrent futures
# def do_sleep(secs):
#     time.sleep(secs)
#     return 'Done Sleeping'
#
#
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     results = [executor.submit(do_sleep, 1) for _ in range(10)]
#
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())


# simple sleep with concurrent.futures
# def do_sleep(secs):
#     time.sleep(secs)
#     return "Done!"
#
#
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     f1 = executor.submit(do_sleep, 1)
#     print(f1.result())


# Sleep example
# def do_sleep(secs):
#     print("Started to sleep")
#     time.sleep(secs)
#
#
# threads = []
# for _ in range(40):
#     t = Thread(target=do_sleep, args=[2,])
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()

# Simple mechanic threads
# t1 = Thread(target=do_sleep, args=[2, ])
# t2 = Thread(target=do_sleep, args=[2, ])
# t3 = Thread(target=do_sleep, args=[2, ])
#
# t1.start()
# t2.start()
# t3.start()
#
# t1.join()
# t2.join()
# t3.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} second(s)')



