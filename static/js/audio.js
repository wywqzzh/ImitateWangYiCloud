;(function (root) {
    const doc = document;
    const addEventListener = root.addEventListener;
    const removeEventListener = root.removeEventListener;
    const tools = {
        // 节点创建
        createEle: function (className, tag) {
            tag = tag || 'div';
            const node = doc.createElement(tag);
            node.className = className;
            return node;
        },
        // 批量节点添加
        append: function (node, child) {
            if (!node) return;
            child = Array.isArray(child) ? child : (child ? [child] : []);
            child.forEach(item => {
                item && item.nodeType ? node.appendChild(item) : null;
            });
        },
        // 事件绑定
        on: function (target, events) {
            if (!target || !events || !Object.keys(events)) return;
            Object.keys(events).forEach(function (ev) {
                target.addEventListener(ev, function (event) {
                    events[ev].call(this, event);
                });
            });
        },
        formatTime: function (time) {
            let formatTime = null,
                secs = 0,
                mins = 0,
                hours = 0,
                displayHours,
                seperator = ':';

            secs = parseInt(time % 60);
            mins = parseInt((time / 60) % 60);
            hours = parseInt(((time / 60) / 60) % 60);
            displayHours = (parseInt(((time / 60) / 60) % 60) > 0)
            secs = ("0" + secs).slice(-2);
            mins = ("0" + mins).slice(-2);
            return (displayHours ? hours + ':' : '') + mins + seperator + secs;
        }
    };

    /**
     * audio: audio element
     * srcs：歌曲列表
     * controller: 控制区域对象
     * volume: 声音对象
     * isPlaying: 播放状态
     * currentIndex: 当前src源的下标
     * meta: 视频元数据
     */
    var script = document.getElementsByTagName("script");
    eval(script[1].innerHTML);
    const Audio = function () {
        this.audio = null;
        this.srcs = args["URLS"];
        this.controller = null;
        this.progress = null;
        this.volume = null;
        this.isPlaying = false;
        this.currentIndex = 0;
        this.meta = {
            currentTime: 0,
            duration: 0
        };
        this.init();
    };

    Audio.prototype = {
        // 构建视图 + 事件绑定
        init: function () {
            this.audio = this.createAudio();
            this.controller = new Controller(this);
            this.progress = new Progress(this);
            this.volume = new Volume(this);
            const container = doc.querySelector('.audio');
            tools.append(container, [
                this.controller.controllerArea,
                this.progress.progressDOM,
                this.volume.volumeArea
            ]);
            this.onEvents();
        },
        // 创建audio对象
        createAudio: function () {
            const audio = tools.createEle('audio-player', 'audio');
            audio.src = this.srcs[this.currentIndex];
            audio.preload = 'auto';
            return audio;
        },
        // 处理事件绑定
        onEvents: function () {
            const that = this;
            const {formatTime} = tools;
            tools.on(this.audio, {
                // 元数据导入事件
                'loadedmetadata': function () {
                    that.meta.duration = this.duration;
                    that.progress.changeEndTime(formatTime(this.duration));
                },
                // 播放过程时间改变事件
                'timeupdate': function () {
                    const meta = that.meta;
                    meta.currentTime = this.currentTime;
                    that.progress.changeCurrentTime(formatTime(this.currentTime));
                    // 计算当前时间占总时间的百分比，以此计算对应的位置
                    const percent = (this.currentTime / meta.duration).toFixed(6) * 100;
                    that.progress.setCurrentProgress(percent);
                },
                // 播放结束事件
                'ended': function () {
                    that.next();
                }
            });
        },
        changeCurrentSrc: function () {
            const audio = this.audio;
            audio.src = this.srcs[this.currentIndex];
            audio.load();
        },
        play: function () {
            this.audio.play();
            this.isPlaying = true;
            words();
            var SNAM=args["SNAMES"][this.currentIndex];
            var VNAME=args["VNAMES"][this.currentIndex];
            console.log("SNAME"+SNAM);
            console.log("VNAME"+VNAME);
            var SN=document.getElementById('SNAME');
            var VN=document.getElementById('VNAME')
            SN.innerHTML=SNAM;
            VN.innerHTML=VNAME;
        },
        pause: function () {
            this.audio.pause();
            this.isPlaying = false;
        },
        prev: function () {
            const targetIndex = this.currentIndex - 1;
            this.currentIndex = targetIndex < 0 ? this.srcs.length - 1 : targetIndex;
            this.changeCurrentSrc();
            this.play();
        },
        next: function () {
            const targetIndex = this.currentIndex + 1;
            this.currentIndex = targetIndex > this.srcs.length - 1 ? 0 : targetIndex
            this.changeCurrentSrc();
            this.play();
        },
        setCurrentTime: function (percent) {
            percent = percent || 0;
            this.audio.currentTime = this.meta.duration * percent;
        },
        setCurrentVolume: function (volume) {
            this.audio.volume = volume || 0;
        }
    };

    /**
     * 控制区域对象
     */
    const Controller = function ($parent) {
        this.$parent = $parent;
        this.controllerArea = null;
        this.prevIcon = null;
        this.stateIcon = null;
        this.nextIcon = null;
        this.isPlaying = false;
        this.init();
    };

    Controller.prototype = {
        init: function () {
            const {createEle, append} = tools;
            const container = createEle('audio-controller');
            this.prevIcon = createEle('fa fa-step-backward icon__back', 'i');
            this.stateIcon = createEle('fa fa-play icon__state', 'i');
            this.nextIcon = createEle('fa fa-step-forward icon__next', 'i');
            append(container, [this.prevIcon, this.stateIcon, this.nextIcon]);
            this.controllerArea = container;
            this.onEvents();
        },
        changeStateIcon: function () {
            const {isPlaying, stateIcon} = this;
            const currentClass = isPlaying ? 'fa-pause' : 'fa-play';
            const targetClass = !isPlaying ? 'fa-pause' : 'fa-play';
            stateIcon.className = stateIcon.className.replace(currentClass, targetClass);
        },
        changeState: function () {
            this.isPlaying = !this.isPlaying;
        },
        onEvents: function () {
            const that = this;
            const {on} = tools;
            // 上一首
            on(this.prevIcon, {
                'click': function () {
                    that.$parent.prev();
                }
            });
            // 下一首
            on(this.nextIcon, {
                'click': function () {
                    that.$parent.next();
                }
            });
            // 播放、暂停功能实现
            on(this.stateIcon, {
                'click': function () {
                    that.changeStateIcon();
                    that.changeState();
                    that.isPlaying ? that.$parent.play() : that.$parent.pause();
                }
            })
        }
    };

    /**
     * 滑动条对象
     * @param {*} $parent
     * @param {*} isBuffer 区分声音控制还是进度控制
     * @param {*} currentPosition 滑块当前位置
     */
    const Slider = function ($parent, isBuffer, currentPosition) {
        this.$parent = $parent;
        this.sliderBox = null;
        this.progressBox = null;
        this.thumbBox = null;
        this.isBuffer = isBuffer || false;
        this.isDragging = false;
        this.startX = 0;
        this.startPosition = currentPosition || 0;
        this.currentPosition = currentPosition || 0;
        this.currentValue = 0;
        this.init();
    };

    Slider.prototype = {
        init: function () {
            const {createEle, append} = tools;
            const sliderBox = createEle('slider');
            const sliderProgress = createEle('slider-progress');
            const runway = createEle('slider-runway');
            append(runway, createEle('thumb'));
            append(sliderBox, [sliderProgress, runway]);
            if (this.isBuffer) {
                append(sliderProgress, createEle('progress-buffer'));
            }
            this.sliderBox = sliderBox;
            this.progressBox = sliderProgress;
            this.thumbBox = runway;
            if (this.currentPosition) {
                this.updateView();
            }
            this.onEvents();
        },
        onEvents: function () {
            const that = this;
            const {thumbBox, sliderBox} = this;
            const {on} = tools;
            on(thumbBox, {
                // 滑动功能的实现依赖：mousedown、mousemove、mouseup事件
                'mousedown': function (event) {
                    event.stopPropagation();
                    that.dragStart(event);
                    addEventListener('mousemove', function (e) {
                        that.dragging(e);
                    });
                    addEventListener('mouseup', function () {
                        that.dragEnd();
                    });
                }
            });
            on(sliderBox, {
                'click': function (event) {
                    const contentBox = this.getBoundingClientRect();
                    const percent = (event.clientX - contentBox.left) / contentBox.width * 100;
                    that.currentPosition = Math.max(0, Math.min(percent, 100));
                    that.updateView();
                    that.changeAudioAbort();
                }
            });
        },
        // 根据点击位置计算对应时间或音量
        changeAudioAbort: function () {
            let percent = this.currentPosition * 0.01;
            if (this.isBuffer) {
                this.$parent.changeAudioCurrTime(percent);
            } else {
                const volume = Math.max(0, Math.min(percent.toFixed(1), 1));
                this.$parent.setCurrentVolume(volume);
            }
        },
        // 更新视图
        updateView: function () {
            const {thumbBox, progressBox} = this;
            const currentPosition = this.currentPosition;
            this.currentValue = Math.floor(currentPosition);
            thumbBox.style.left = currentPosition + '%';
            progressBox.style.width = currentPosition + '%';
        },
        changeCurrentPosition: function (position) {
            if (this.isDragging) return;
            this.currentPosition = position || 0;
            this.updateView();
        },
        setPosition: function (clientX) {
            const {sliderBox, thumbBox} = this;
            const contentWidth = sliderBox.offsetWidth;
            // 计算当前拖动位置与初始拖动位置的距离
            const diff = clientX - this.startX;
            // 计算差距占精度条的百分比
            const percent = (diff / contentWidth).toFixed(6) * 100;
            this.currentPosition = Math.max(0, Math.min(
                this.startPosition + percent, 100));
            this.updateView();
        },
        dragStart: function (event) {
            this.isDragging = true;
            // 记录开始滑动时clientX
            this.startX = event.clientX;
            // 记录当前位置为开始值
            this.startPosition = this.currentPosition;
        },
        dragging: function (event) {
            if (!this.isDragging) return;
            this.setPosition(event.clientX);
            // 进度在拖动过程中不改变当前播放进度
            // 音量设置立即改变
            if (!this.isBuffer) {
                this.changeAudioAbort();
            }
        },
        dragEnd: function () {
            this.changeAudioAbort();
            this.isDragging = false;
            removeEventListener('mousemove', this.dragging);
            removeEventListener('mouseup', this.dragEnd);
        }
    };


    const Progress = function ($parent) {
        this.$parent = $parent;
        this.slider = new Slider(this, true);
        this.progressDOM = null;
        this.curTimeDOM = null;
        this.endTimeDOM = null;
        this.currentTime = '00:00';
        this.endTime = '00:00';
        this.init();
    };

    Progress.prototype = {
        init: function () {
            const {createEle, append} = tools;
            const curTimeDOM = createEle('time__current', 'span');
            const endTimeDOM = createEle('time__end', 'span');
            const progress = createEle('audio-progress');
            const sliderContainer = createEle('slider-container');
            append(sliderContainer, this.slider.sliderBox);
            append(progress, [
                curTimeDOM,
                sliderContainer,
                endTimeDOM
            ]);
            this.curTimeDOM = curTimeDOM;
            this.endTimeDOM = endTimeDOM;
            this.setCurrentTimeText();
            this.setEndTimeText();
            this.progressDOM = progress;
        },
        changeCurrentTime: function (currentTime) {
            this.currentTime = currentTime;
            this.setCurrentTimeText();
        },
        changeEndTime: function (endTime) {
            this.endTime = endTime;
            this.setEndTimeText();
        },
        setCurrentTimeText: function () {
            this.curTimeDOM.innerText = this.currentTime;
        },
        setEndTimeText: function () {
            this.endTimeDOM.innerText = this.endTime;
        },
        setCurrentProgress: function (percent) {
            this.slider.changeCurrentPosition(percent);
        },
        changeAudioCurrTime: function (percent) {
            this.$parent.setCurrentTime(percent);
        }
    };

    const Volume = function ($parent) {
        this.$parent = $parent;
        this.currentValue = 0.5;
        this.max = 1;
        this.min = 0;
        this.volumeArea = null;
        this.slider = new Slider(this, false, this.currentValue * 100);
        this.init();
    };

    Volume.prototype = {
        init: function () {
            const {createEle, append} = tools;
            const i = createEle('fa fa-volume-up icon__volume', 'i');
            const box = createEle('audio-volume');
            append(box, [i, this.slider.sliderBox]);
            this.volumeArea = box;
        },
        setCurrentVolume: function (volume) {
            this.currentValue = volume;
            this.$parent.setCurrentVolume(volume);
        }


    };

    // new Audio();
    var x = new Audio();
    x.controller.changeStateIcon();
    x.controller.changeState();
    x.controller.isPlaying ? x.controller.$parent.play() : x.controller.$parent.pause();
    x.play();

    function words() {
        var script = document.getElementsByTagName("script");
        eval(script[1].innerHTML);
        // console.log(args["URLS"]);
        // console.log(args["IRCS"]);
        // console.log(args["SNAMES"]);
        // console.log(args["VNAMES"]);
        var lrcJSON = args["IRCS"][x.currentIndex];
        console.log("Index:",x.currentIndex)
        console.log(lrcJSON);
        /*var lrcJSON = {
            "[00:01.000]": " 作词 : 陈曦",
            "[00:06.530]": "",
            "[00:07.230]": "男：",
            "[00:07.970]": "谁面前 一片云里雾里的山",
            "[00:14.400]": "",
            "[00:15.320]": "推开门 我是看风景的人",
            "[00:20.680]": "",
            "[00:22.480]": "转一圈 见仙外仙见天外天",
            "[00:29.710]": "",
            "[00:30.230]": "天地间 我牵挂的是那一眼",
            "[00:35.940]": "",
            "[00:36.510]": "女：",
            "[00:37.520]": "那一卷 泼墨留白的分寸感",
            "[00:44.860]": "千百遍 我在心里默念",
            "[00:51.300]": "",
            "[00:52.430]": "绕一圈 那些年的悟道参禅",
            "[00:59.360]": "",
            "[00:59.990]": "你面前 始终无法说圆",
            "[01:06.730]": "男：",
            "[01:07.890]": "看一看 前路弯弯",
            "[01:11.490]": "见一见 花落池边",
            "[01:15.170]": "听一听 弹欲断弦",
            "[01:20.400]": "女：",
            "[01:22.710]": "会一会 地阔天圆",
            "[01:26.500]": "转一转 尘世凡间",
            "[01:30.250]": "",
            "[01:30.790]": "只不过 一念之间",
            "[01:36.230]": "",
            "[01:36.830]": "男：",
            "[01:38.040]": "你来过 我记得  便是永远",
            "[01:44.120]": "",
            "[01:45.160]": "如一缕青烟 挥之不去 终日缠绵",
            "[01:52.270]": "女：",
            "[01:52.820]": "你转身 我经过  便是人间",
            "[02:00.180]": "如一滴水恋你指尖 万般不愿",
            "[02:10.370]": "",
            "[02:23.570]": "女：",
            "[02:26.320]": "那一卷 泼墨留白的分寸感",
            "[02:33.450]": "千百遍 我在心里默念",
            "[02:39.590]": "男：",
            "[02:41.250]": "绕一圈 那些年的悟道参禅",
            "[02:48.180]": "",
            "[02:48.960]": "你面前 始终无法说圆",
            "[02:55.450]": "合：看一看",
            "[02:58.040]": "男：前路弯弯",
            "[03:00.180]": "合：见一见",
            "[03:01.410]": "男：花落池边",
            "[03:03.410]": "合：听一听",
            "[03:05.460]": "男：弹欲断弦",
            "[03:09.170]": "合：会一会",
            "[03:12.820]": "女：地阔天圆",
            "[03:14.700]": "合：转一转",
            "[03:16.380]": "女：尘世凡间",
            "[03:18.400]": "合：只不过 一念之间",
            "[03:25.520]": "男：你来过 我记得",
            "[03:29.470]": "合：便是永远",
            "[03:32.510]": "男：如一缕青烟 挥之不去",
            "[03:37.310]": "合：终日缠绵",
            "[03:41.000]": "女：你转身 我经过",
            "[03:44.670]": "合：便是人间",
            "[03:48.130]": "女：如一滴水恋你指尖",
            "[03:52.790]": "合：万般不愿",
            "[03:58.410]": "",
            "[03:59.850]": "男：你来过",
            "[04:01.040]": "女：来过",
            "[04:02.160]": "男： 我记得",
            "[04:03.650]": "合： 便是永远",
            "[04:07.590]": "如一缕青烟 挥之不去 终日缠绵",
            "[04:14.970]": "男：你转身 我经过  便是人间",
            "[04:21.830]": "女： 如一滴水",
            "[04:25.790]": "男： 恋你指尖",
            "[04:29.150]": "合： 心甘情愿",

        };*/
        var lrcTime = [];//歌词对应的时间数组
        var ul = $("#lrclist")[0];//获取ul

        var i = 0;
        ul.innerHTML=null;
        $.each(lrcJSON, function (key, value) {//遍历lrc
            lrcTime[i++] = parseFloat(key.substr(1, 3)) * 60 + parseFloat(key.substring(4, 10));//00:00.000转化为00.000格式
            ul.innerHTML += "<li><p>" + lrcJSON[key] + "</p></li>";//ul里填充歌词
        });
        lrcTime[lrcTime.length] = lrcTime[lrcTime.length - 1] + 3;//如不另加一个结束时间，到最后歌词滚动不到最后一句


        var $li = $("#lrclist>li");//获取所有li

        var currentLine = 0;//当前播放到哪一句了
        var currentTime;//当前播放的时间
        var audio = x.audio;
        var ppxx;//保存ul的translateY值

        audio.ontimeupdate = function () {//audio时间改变事件
            currentTime = audio.currentTime;
            for (j = currentLine, len = lrcTime.length; j < len; j++) {
                if (currentTime < lrcTime[j + 1] && currentTime > lrcTime[j]) {
                    currentLine = j;
                    ppxx = 250 - (currentLine * 32);
                    ul.style.transform = "translateY(" + ppxx + "px)";
                    $li.get(currentLine - 1).className = "";
                    $li.get(currentLine).className = "on";
                    break;
                }
            }
        };

        audio.onseeked = function () {//audio进度更改后事件
            currentTime = audio.currentTime;
            console.log("  off" + currentLine);
            $li.get(currentLine).className = "";
            for (k = 0, len = lrcTime.length; k < len; k++) {
                if (currentTime < lrcTime[k + 1] && currentTime < lrcTime[k]) {
                    currentLine = k;
                    break;
                }
            }
        };
    }


})(window);