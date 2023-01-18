HELP_MSG = '''Commands:
/help | /start - show help message
/reply [msg] - reply echo
/answer [msg]- answer echo
/delete [msg]- delete message
/advice - get a good adwice
/cat - get a funny cat img
'''

LMAO = [
    'LOOOL',
    'LMAO',
    'AHAHAHAHA',
    'OMG',
    'XD',
    'FUNNY',
    'OHOHOHOHO',
]

ADVICES = [
    'If someone asks you for advice, you should do your best to help.',
    'Your friend has tried to choose you a great present, so you ought to thank her even if you dont like it.',
    'I really dont think you should take part in the auction tomorrow.',
    'If I were you, I would buy a new pair of shoes every week.',
    'If it happened to me, I would call the police straight away.',
    'If I had that problem, Id see a doctor.',
    'In my experience, doing morning exercises regularly works really well.',
    'I would suggest going for a run and getting all the problems out of your head.',
    'I would recommend skiing for an hour every Sunday.',
    'My personal recommendation would be to improve your basic language skills before going abroad.',
    'I would always recommend that everyone use paper bags rather than plastic ones.',
    'Youd better not eat so much spicy food or you will get heartburn.',
]

CATS_IMGS = [
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxpAANDD5lp40PFYJlZSAFrrweJGG97P4nNzIysQYMSZBdJzomMy_1YVW3SURuCjTD1LE&usqp=CAU',
    'https://newstes.ru/uploads/posts/2022-07/prosto-smeshnye-koty-15-foto-4.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRV1iebmfo7pIlUO6QO4xuw1g8HVptgEi6NQ&usqp=CAU',
    'https://img.novosti-n.org/upload/ukraine/1029782.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuSxXeGCWAypDDeM6TF_9ge9iTqpqp4Wvs94cH-bzWDLsOk7_noyUO0lWpf8RiIKWvrEk&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuK_uEj6Ydd7KiRu-kvOoWCwD7DbsGhgHZ-TkjOPCCcgkM_K4Bu9b8WHThpnir7zJYPhY&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVw9AQdyk5SgUdhv_r_dMNXCYf2md3492COA&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3sFw1jkJe8Gc7sjr7voc9Q9RBTbRnlenWmQ&usqp=CAU',
    'https://avatars.dzeninfra.ru/get-zen_doc/108343/pub_5b9bc3e60a646400aa3ffb61_5b9bc458b76d9000aa06f1e7/scale_1200',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1Ruv3lY9P7i-E7FXYt8ApgQXK6wAQqD3cmw&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTN9RLW568wwKbyHwa-_syg115O0UwL86E0vg&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREOOEbQPF1Tf4xlODDRXA5qglcsLFYVxMz9g&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQw5KKN4MNO66LUAKrNdolFqqEMtYkhgVOJfQ&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQD04wx7HAnePXq2yagxFuFFrjcYHJT0olm7A&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQM0GxS5xj-BggIDFPp6wymP4RxXMDPM9OD4A&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTz8iqXCbCpPRevu2XOSjI8IS1A1WXJ9yhBPA&usqp=CAU',
    'https://ololo.tv/wp-content/uploads/2018/06/d0ff1c882d.jpg',
    'https://cn1.nevsedoma.com.ua/images/2011/130/2/dressed_.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBI1mQk6OpWAMIvXzhjwaYZI-sgwCVqBQkAQ&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR9lnwcfCLSvPexi2N2apd0g_xn7wTYkqZt4Ne-YGSfmaSmjiRZJM0WlNYBKyL1GJUQbo8&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXWrZgSLiMz-13Zo5lll86dj1_vOXyHso_NKG2msknp6hZHi1I05kEPyexDPifBAZWfCM&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDBHIZY5FhVKgDXg-VZAc8wcyjLBg8Cod7t18Dfk1V9cKL6H7rGPH8NcLALYM9POUTMNQ&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUFWA0Ws84tk2oy5P73aFHrczPmiWdWLYo6UvPw9yQ2JIsaYFoY4jlIS10iZJLUsXotbo&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1RnQ6aRKI6r2M_l7jum8F0gfUr-JCldCk6Z_Fg29EiQjl4PG3O1fjjZM5jzOEWD_ARJs&usqp=CAU',
    'https://i.pinimg.com/564x/f5/4f/13/f54f13638f0941531c46b817022065bb.jpg',
    'https://avatars.dzeninfra.ru/get-zen_doc/3985746/pub_637c7c05d7971e0d378ae59f_637f1aa019398772ed547f6d/scale_1200',
    'https://kotsf.ru/wp-content/uploads/2020/02/f222ce3e08376ced9dae7f03557091ba.jpg',
    'https://cs8.pikabu.ru/post_img/big/2018/01/23/7/1516702880178892189.jpg',
    'https://www.meme-arsenal.com/memes/871ad0cf10895c4cb8cf07d1afea93c9.jpg',
    'https://kaifolog.ru/uploads/posts/2013-03/thumbs/1363239460_010.jpg',
    'https://www.rulez-t.info/uploads/posts/2020-05/1590900680_smeshnye-koty-1.jpg',
    'https://i.ytimg.com/vi/M-XtB0R3ri4/maxresdefault.jpg',
    'https://www.povarenok.ru/data/cache/2013oct/24/37/542210_44087-640x0.jpg',
    'https://lifeglobe.net/x/entry/6080/1-0.jpg',
    'https://zefirka.net/wp-content/uploads/2017/06/smeshnye-koty-kotorye-otkazyvayutsya-vesti-sebya-kak-normalnye-zhivotnye-1.jpg',
    'https://kaifolog.ru/uploads/posts/2013-03/thumbs/1363239460_010.jpg',
    'https://kids-tube.ru/pic/70/yq7_17AGYEI.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQL4vdN93jtviAd0DBdmDuuhTW_vyLGUpAxdA&usqp=CAU',
    'https://bugaga.ru/uploads/posts/2014-05/1399017802_smeshnye-pushistiki-5.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQw-6LLBRKszNpcBXvXOkqJvT8ues9YmMmMg&usqp=CAU',
    'https://bigpicture.ru/wp-content/uploads/2019/01/rojiman01.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyrziqixknOb4-2FTJr9R4fZmPR4ncbk-wOw&usqp=CAU',
    'https://avatars.dzeninfra.ru/get-zen_doc/1917783/pub_5fd45fa20b82510af5a792f7_5fd45ffb9480ec78dc2c1518/scale_1200',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRs6nROU5aMcSpbQTubMfwFgzZly5VS6VFEFQ&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqg-z1QHtmJo9xgGKJe7Hr8wPgXjkowcRVNA&usqp=CAU',
    'https://smotrim.net/uploads/posts/2020-06/smotrim.net_prikolnye-koty-kotorye-sidjat-kak-ljudi-19-foto-1.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZFME05Xv1E8PyhQuq7bMx_A1GLjghl22pBg&usqp=CAU',
    'https://avatars.dzeninfra.ru/get-zen_doc/237236/pub_5bdd9af1b327ef00a937453f_5bdd9c4344fea400aaec212d/scale_1200',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTYNG7IaargWEzWdSbj50RtzEYgDXimo9Ak1Q&usqp=CAU',
    'https://i.pinimg.com/736x/76/55/6b/76556bd39454db292eed9bb23b315f5e.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVkTONfe5Z1eF-DF0-9sEEjYfkvGlcE2bLXA&usqp=CAU',
]
