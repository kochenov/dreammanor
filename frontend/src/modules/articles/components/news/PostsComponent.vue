<template>
  <div v-if="articlesStore.news" class="row-grid">
    <q-card
      v-for="i in articlesStore.news"
      :key="i.id"
      class="my-card"
      flat
      bordered
    >
      <q-card-section
        style="flex: 1 0 auto; justify-content: space-between"
        horizontal
      >
        <q-card-section
          class="flex q-pt-xs"
          style="align-content: flex-start; flex-direction: column"
        >
          <div class="text-caption">
            <q-chip
              clickable
              size="sm"
              square
              icon="folder"
              @click="$router.push('/news/category/' + i.category.id)"
              :label="i.category.name"
            />
          </div>
          <div class="q-mt-sm q-mb-xs">
            <router-link
              class="text-h6 title text-dark"
              :to="'/news/category/' + i.category_id + '/post/' + i.id"
              >{{ i.title }}</router-link
            >
          </div>
          <div class="text-caption text-grey">
            {{ i.short_description }}
          </div>
        </q-card-section>

        <q-card-section class="col-lg-5 flex flex-center">
          <q-img
            class="rounded-borders"
            src="https://cdn.quasar.dev/img/parallax2.jpg"
          />
        </q-card-section>
      </q-card-section>

      <q-separator />

      <q-card-actions align="between">
        <q-btn
          flat
          size="sm"
          dense
          color="primary"
          icon="calendar_month"
          :label="date.formatDate(i.created_ad, 'DD MMM YYYY HH:mm:ss')"
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
            {{ i.count_views }}
            {{
              wordNum(i.count_views, ["просмотр", "просмотра", "просмотров"])
            }}
          </q-tooltip>
        </q-btn>
        <q-btn
          size="sm"
          flat
          dense
          color="primary"
          class="gt-sm"
          icon="person"
          label="Дмитрий"
        />

        <q-btn
          size="sm"
          dense
          color="primary"
          :to="'/news/category/' + i.category_id + '/post/' + i.id"
          outline
          icon-right="arrow_right_alt"
        />
      </q-card-actions>
    </q-card>
  </div>
  <div class="q-mt-xl">
    <div class="flex flex-center">
      <q-pagination
        v-if="Math.ceil(articlesStore.count_news / articlesStore.limit) >= 2"
        v-model="current"
        :max="Math.ceil(articlesStore.count_news / articlesStore.limit)"
        :max-pages="Math.ceil(articlesStore.count_news / articlesStore.limit)"
        boundary-numbers
        direction-links
        color="black"
        active-color="yellow"
        active-text-color="black"
      />
    </div>
  </div>
</template>

<script setup>
import { wordNum } from "/src/helpers/word";

import { date } from "quasar";
import { ref, watch, onMounted } from "vue";
//import { useArticlesStore } from "src/stores/all";
import { useRoute, useRouter } from "vue-router";

const route = useRoute();
const router = useRouter();

const current = ref(1);
const offset = ref(0);

const props = defineProps({
  popular: {
    type: Number,
    default: 0,
  },
});

const articlesStore = useArticlesStore();
onMounted(async () => {
  await articlesStore.getAllNews(
    !route.params.cat ? 0 : Number(route.params.cat),
    offset.value,
    props.popular
  );

  if (!articlesStore.cur_cat_news && !articlesStore.news) {
    router.push("/404");
    return;
  }
});
watch(current, async () => {
  offset.value = articlesStore.limit * (current.value - 1);
  await articlesStore.getAllNews(
    !route.params.cat ? 0 : Number(route.params.cat),
    offset.value,
    props.popular
  );
});
</script>

<style lang="scss" scoped>
.my-card {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
}
.row-grid {
  display: grid;

  grid-template-columns: repeat(auto-fill, minmax(470px, 1fr));
  @media (max-width: $breakpoint-sm-max) {
    grid-template-columns: repeat(auto-fit, minmax(270px, 1fr));
  }
  gap: 20px;
  justify-content: center;
}

.title {
  font-size: 16px;
  text-decoration: none;
}
</style>
