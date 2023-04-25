<template>
  <div class="row-grid">
    <q-card class="my-card" flat bordered>
      <q-card-actions align="between">
        <q-btn
          size="sm"
          flat
          dense
          :to="'/news/category/' + articlesStore.news.category.id"
          color="primary"
          class="gt-sm"
          icon="folder"
          :label="articlesStore.news.category.name"
        />
        <q-btn
          flat
          size="sm"
          dense
          color="primary"
          icon="calendar_month"
          :label="created_ad"
        />
        <q-btn
          size="sm"
          flat
          dense
          color="primary"
          class="gt-sm"
          icon="visibility"
        >
          <q-tooltip
            anchor="top middle"
            self="bottom middle"
            :offset="[10, 10]"
          >
            {{ articlesStore.news.count_views }}
            {{
              wordNum(articlesStore.news.count_views, [
                "просмотр",
                "просмотра",
                "просмотров",
              ])
            }}
          </q-tooltip>
        </q-btn>

        <q-btn size="sm" dense color="primary" flat icon="forum">
          <q-tooltip
            anchor="top middle"
            self="bottom middle"
            :offset="[10, 10]"
          >
            {{ articlesStore.news.count_views }}
            {{
              wordNum(articlesStore.news.count_views, [
                "коментарий",
                "коментария",
                "коментариев",
              ])
            }}
          </q-tooltip>
        </q-btn>
      </q-card-actions>
      <q-separator />
      <q-card-section>
        <pre lang="js">{{ articlesStore.news }}</pre>
      </q-card-section>
    </q-card>
    <q-card class="my-card-p">
      <q-img src="https://cdn.quasar.dev/img/parallax2.jpg">
        <div class="absolute-bottom text-subtitle2 text-center">Title</div>
      </q-img>
    </q-card>
  </div>
</template>

<script setup>
import { wordNum } from "/src/helpers/word";

import { ref, onMounted } from "vue";
import { useArticlesStore } from "../../store";
import { useRoute } from "vue-router";
import { date } from "quasar";
const articlesStore = useArticlesStore();
const route = useRoute();
/* const date2 = new Date("2023-01-30 17:06:00").getTime();
const unit = "seconds";

const daTE = ref(date.getDateDiff(Date.now(), date2, unit)); */
const created_ad = ref();

onMounted(async () => {
  //await articlesStore.getPost(route.params.cat, route.params.num);
  created_ad.value = date.formatDate(
    articlesStore.news.created_ad,
    "DD MMM YYYY HH:mm:ss"
  );
});
</script>

<style lang="scss" scoped>
.my-card {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;

  .q-img {
    max-width: 700px;
  }
}
.my-card-p {
  height: fit-content;
}
.row-grid {
  display: grid;

  grid-template-columns: 1fr 250px;
  grid-template-rows: repeat(auto-fit, minmax(40px, 1fr));
  @media (max-width: $breakpoint-sm-max) {
    grid-template-columns: 1fr;
  }
  gap: 20px;
  justify-content: center;
}

.title {
  font-size: 16px;
  text-decoration: none;
}
</style>
