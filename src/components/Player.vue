<template>
    <video controls crossorigin playsinline autoplay poster="@/assets/djavue_player.png" class="embed-responsive-item" ref="player"></video>
</template>

<style scoped>
    @import url('https://cdn.plyr.io/3.6.2/plyr.css');
</style>

<script>
    import Plyr from 'plyr';
    import Hls from 'hls.js';
    export default {
        name: 'Player',
        props: ['source'],
        mounted() {
            let source = this.source;
            let video = this.$refs.player;
            const player = new Plyr(video);
            if (!Hls.isSupported()) {
			    video.src = source;
            } else {
                const hls = new Hls();
                hls.loadSource(source);
                hls.attachMedia(video);
                window.hls = hls;
                
                // Handle changing captions
                player.on('languagechange', () => {
                    setTimeout(() => hls.subtitleTrack = player.currentTrack, 50);
                });
            }
            
            // Expose player so it can be used from the console
            window.player = player;
        }
        
    }
</script>