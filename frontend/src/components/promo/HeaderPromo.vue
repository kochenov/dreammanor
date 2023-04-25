<template>
  <div class="promo">
    <q-carousel
      v-model="slide"
      swipeable
      animated
      arrows
      height="35px"
      class="bg-promo text-white"
    >
      <q-carousel-slide
        name="style"
        class="flex no-wrap overflow-hidden flex-center"
      >
        <div class="text-center test">
          <span>
            Это рекламное обьявление: Это очень длинный текст для примера
          </span>
        </div>
      </q-carousel-slide>
      <q-carousel-slide name="tv" class="flex no-wrap flex-center">
        <div class="text-center">Текст 2</div>
      </q-carousel-slide>
      <q-carousel-slide name="layers" class="flex no-wrap flex-center">
        <div class="text-center">Текст 3</div>
      </q-carousel-slide>
      <q-carousel-slide name="map" class="flex no-wrap flex-center">
        <div class="text-center">Текст 4</div>
      </q-carousel-slide>
    </q-carousel>
  </div>
</template>

<script setup>
import { ref } from "vue";

const slide = ref("style");

defineProps({
  slides: {
    type: String,
    default: null,
  },
});
</script>

<style lang="scss">
.promo {
  font-size: 13px;
  border-top: 0.105rem solid #ffffff;
  @media (max-width: $breakpoint-xs-max) {
    font-size: 10px;
  }
  .flex {
    flex-wrap: nowrap;
  }
  .test {
    margin: 0px 30px;
    //overflow: hidden;
    white-space: nowrap;
    @media (max-width: $breakpoint-xs-max) {
      animation: myAnim 15s infinite linear;
    }
  }
}
@keyframes myAnim {
  0% {
    //opacity: 0;
    transform: translateX(100%);
  }

  100% {
    //opacity: 1;
    transform: translateX(-110%);
  }
}
</style>
