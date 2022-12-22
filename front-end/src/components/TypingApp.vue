<template>
    <v-app>
        <v-card width="400" height="200" class="mx-auto mt-5 ">
            <div class="center">
                <div v-if="playing">
                    <h2>
                        <span>{{ pressed }}</span>{{ word }}
                    </h2>
                    <br>
                    <h2>{{ word_jpn }}</h2>
                </div>
                <div v-else>
                    <v-card-actions class="justify-center">
                        <v-btn class="btn_blur" variant="outlined" v-on:click.once="doStart"><h2>Start</h2></v-btn>
                    </v-card-actions>
                </div>

                <p v-if="playing" style="text-align: right;margin-right: 5px;">{{ idx_now }}枚目</p>
                
            </div>
        </v-card>         
    </v-app>
    
</template>

<script>
export default {
    data() {
        return {
            words: ['apple', 'banana', 'grape'],
            words_jpn: ['りんご', 'バナナ', 'ぶどう'],
            idx:[],
            word: '',
            pressed: '',
            miss: 0,
            playing: false,
            idx_now:0,
        };
    },
    methods: {
        doStart() {
            if (this.playing) {
                return;
            }
            this.playing = true;
            this.idx = this.shuffleIdx();
            this.idx_now = 0;
            this.setWord();
            this.keyDown();
        },
        setWord() {
            this.word = this.words[this.idx[this.idx_now]];
            this.word_jpn = this.words_jpn[this.idx[this.idx_now]];
            this.pronounce()
            console.log(this.idx_now)
            this.idx_now += 1;
        },
        keyDown() {
            addEventListener('keydown', (e) => {
                console.log(this.word)
                if (e.key !== this.word[0]) {
                    return;
                }
                this.pressed += e.key;
                this.word = this.word.slice(1);
                if (this.word.length === 0) {
                    this.pressed = '';
                    if (this.idx_now === this.words.length) {
                        this.word = 'FINISH';
                        this.word_jpn = "";
                        this.playing = false
                        return;
                    }
                    this.setWord();
                }
            });
        },
        shuffleIdx() {
            const array = [...Array(this.words.length)].map((_, i) => i) //=> [ 0, 1, 2, 3, 4 ]
            for (let i = array.length - 1; i >= 0; i--) {
                let rand = Math.floor(Math.random() * (i + 1));
                [array[i], array[rand]] = [array[rand], array[i]]
            }
            console.log(array)
            return array;
        },
        pronounce() {
            if ('speechSynthesis' in window) {
                const sound = new SpeechSynthesisUtterance()
                sound.lang = "en-GB";
                sound.text = this.word;
                sound.pitch = 1.0;
                sound.rate = 1.0;
                speechSynthesis.speak(sound)
                
            }
        }
    },
};
</script>

<style scoped>
.center {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}
.gray{
    background-color: rgb(118, 112, 118);
}
span {
    color:blue; 
    opacity: 0.8;
}
.btn_blur{
    /* color: blue; */
    background-color: beige;
}
</style>