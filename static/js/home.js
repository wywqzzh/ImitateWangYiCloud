<
script >
window.onload = function () {
        {
            #var
            imgs = document.getElementsByTagName('img');
            #
        }
        {
            #var
            out = document.getElementById('imgList');
            #
        }
        {
            #out.style.width = 1100 * imgs.length + "px";
            #
        }
        var nav = document.getElementById('nav');
        var imgCarousel = document.getElementById('imgCarousel');
        nav.style.left = (imgCarousel.offsetWidth - nav.offsetWidth) / 2 + "px";

        var allA = nav.getElementsByTagName('a');
        var allImg = ['../static/imgs/Carousel/1.jpg', '../static/imgs/Carousel/2.jpg', '../static/imgs/Carousel/3.jpg', '../static/imgs/Carousel/4.jpg', '../static/imgs/Carousel/5.jpg']
        var allHref = ['https://www.baidu.com/', 'https://www.jiaoyimao.com/', 'https://music.163.com/', 'http://www.uu898.com/', 'https://www.qq.com/'];
        var index = 0;
        allA[index].style.backgroundColor = 'red';
        for (var i = 0; i < allA.length; i++) {
            allA[i].index = i;
            allA[i].onclick = function () {
                index = this.index;
                var IMG = imgCarousel.getElementsByTagName('img')[0];
                var imgCarousel_a = document.getElementById('imgCarousel_a');
                console.log(imgCarousel_a.innerHTML);
                imgCarousel_a.href = allHref[index];
                IMG.src = allImg[index];

                for (var i = 0; i < allA.length; i++) {
                    allA[i].style.backgroundColor = '';
                }
                allA[index].style.backgroundColor = 'red';
            }
        }
        change();

        function change() {
            setInterval(function () {
                var IMG = imgCarousel.getElementsByTagName('img')[0];
                index = (index + 1) % (allA.length);
                var imgCarousel_a = document.getElementById('imgCarousel_a');
                imgCarousel_a.href = allHref[index];
                IMG.src = allImg[index];
                for (var i = 0; i < allA.length; i++) {
                    allA[i].style.backgroundColor = '';
                }
                allA[index].style.backgroundColor = 'blue';
            }, 3000)
        }
    }