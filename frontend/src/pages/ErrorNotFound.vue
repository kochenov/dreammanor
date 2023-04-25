<template>
  <div
    class="fullscreen bg-blue text-white text-center q-pa-md flex flex-center"
  >
    <div>
      <div style="font-size: 30vh">404</div>

      <div class="text-h2" style="opacity: 0.4">
        Опс. Страницы не существует...
      </div>

      <q-btn
        class="q-mt-xl"
        color="white"
        text-color="blue"
        unelevated
        to="/"
        label="Перейти на главную"
        no-caps
      />
    </div>
  </div>
</template>

<script setup>
import { defineComponent } from "vue";
import { useMeta } from "quasar";

const metaData = {
  title: "Такой страницы не существует",
  meta: {
    robots: { name: "robots", content: "noindex" },
  },
};

useMeta(metaData);
</script>
