<template>
  <v-app class="typing-bg">
    <v-card width="400" height="220" class="mx-auto mt-5">
      <div>
        <div v-if="playing == 0" class="center">
          <v-card-actions class="justify-center">
            <v-btn v-on:click.once="doStart" style="margin-top: 40px">
              <h2>Start</h2>
            </v-btn>
          </v-card-actions>
        </div>
        <div v-else-if="playing == 1">
          <v-sheet class="dark-center">
            <h1 class="word center">
              <span>{{ pressed }}</span
              >{{ word }}
            </h1>
          </v-sheet>
          <br />
          <h2 class="center-lr">{{ word_jpn }}</h2>
          <v-progress-linear
            v-bind:model-value="percent_now"
            class="progress_bar"
          ></v-progress-linear>
        </div>
        <div v-else-if="playing == 2">
          <h1 class="center" style="margin-top: 80px">FINISH</h1>
        </div>
      </div>
    </v-card>
    <div v-if="playing == 2">
      <v-sheet class="sheet">
        <v-container>
          <v-row class="ma-8">
            <transition-group name="list">
              <v-col
                v-for="(item, index) in words"
                :key="item"
                class="list-item"
                cols="3"
              >
                <v-card height="170" class="ma-8" color="">
                  <h2 class="text-center inner-center">{{ item }}</h2>
                  <h3 class="text-center inner-center">
                    {{ words_jpn[index] }}
                  </h3>
                  <v-switch
                    v-model="words_id_weak"
                    color="primary"
                    v-bind:value="words_id[index]"
                    class="switch"
                  >
                  </v-switch>
                </v-card>
              </v-col>
            </transition-group>
          </v-row>
        </v-container>
      </v-sheet>
      <p>{{ this.words_id_weak }}</p>
    </div>
  </v-app>
</template>

<script>
import axios from "axios";
export default {
  props: ["level"],
  data() {
    return {
      words: ["apple", "banana", "grape"],
      words_jpn: ["りんご", "バナナ", "ぶどう"],
      words_id: [1, 2, 3],
      words_id_weak: [],
      idx: [],
      word: "",
      pressed: "",
      miss: 0,
      playing: 2, // 0:before 1:ongoing 2:after
      idx_now: 0,
      percent_now: 0,
      aaa: [],
    };
  },
  mounted() {
    const URL = "http://localhost:8000/word_list/set";
    axios
      .get(URL, {
        params: {
          word_num: 5,
          word_level: this.level,
        },
      })
      .then((response) => {
        this.words = response.data.map(function (item) {
          return item["English_word"];
        });
        this.words_jpn = response.data.map(function (item) {
          return item["Japanese_word"];
        });
        this.words_id = response.data.map(function (item) {
          return item["id"];
        });
      })
      .catch((err) => {
        console.log(err);
      });
  },
  methods: {
    doStart() {
      if (this.playing) {
        return;
      }
      // console.log("level",this.level)
      console.log(this.words);
      console.log(this.words_id);
      this.playing = 1;
      this.idx = this.shuffleIdx();
      this.idx_now = 0;
      this.setWord();
      this.keyDown();
    },
    setWord() {
      this.word = this.words[this.idx[this.idx_now]];
      this.word_jpn = this.words_jpn[this.idx[this.idx_now]];
      this.word_id = this.words_id[this.idx[this.idx_now]];
      this.pronounce();
      // console.log(this.idx_now)
      this.idx_now += 1;
      this.percent_now = Math.round((this.idx_now / this.words.length) * 100);
      // console.log(this.percent_now);
    },
    keyDown() {
      addEventListener("keydown", (e) => {
        if (e.key !== this.word[0]) {
          return;
        }
        this.pressed += e.key;
        this.word = this.word.slice(1);
        if (this.word.length === 0) {
          this.pressed = "";
          if (this.idx_now === this.words.length) {
            this.word = "FINISH";
            this.word_jpn = "";
            this.playing = 2;
            return;
          }
          this.setWord();
        }
      });
    },
    shuffleIdx() {
      const array = [...Array(this.words.length)].map((_, i) => i); //=> [ 0, 1, 2, 3, 4 ]
      for (let i = array.length - 1; i >= 0; i--) {
        let rand = Math.floor(Math.random() * (i + 1));
        [array[i], array[rand]] = [array[rand], array[i]];
      }
      return array;
    },
    pronounce() {
      if ("speechSynthesis" in window) {
        const sound = new SpeechSynthesisUtterance();
        sound.lang = "en-GB";
        sound.text = this.word;
        sound.pitch = 1.0;
        sound.rate = 1.0;
        speechSynthesis.speak(sound);
      }
    },
    debug() {
      console.log(this.words_id_weak);
    },
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
  margin-top: 40px;
}

span {
  color: blue;
  opacity: 0.8;
}
.btn_blur {
  /* color: blue; */
  background-color: #96dccb;
}
.progress_bar {
  color: rgb(25, 171, 115);
  margin-top: 20px;
}
.inner-center {
  margin-top: 30px;
}
.sheet {
  margin: 10px;
  background-color: rgb(231, 225, 227);
}
.word {
  color: rgb(247, 247, 247);
  /* -webkit-text-stroke: 1px #000; */
}
.dark-center {
  background-color: rgb(57, 56, 56);
  margin-left: 10px;
  margin-right: 10px;
  margin-top: 10px;
  height: 120px;
  position: inherit;
  overflow: hidden;
}
.center-lr {
  text-align: center;
}
.switch {
  /* display: flex;
  justify-content: flex-end; */
  margin-left: 85%;
}
</style>
