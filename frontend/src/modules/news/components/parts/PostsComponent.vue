<template>
  <q-inner-loading :showing="load">
    <q-spinner-gears size="50px" color="primary" />
  </q-inner-loading>
  <div v-if="!load" class="row-grid">
    <q-card v-for="i in posts" :key="i.id" class="my-card" flat bordered>
      <q-card-section
        style="
          flex: 1 0 auto;
          justify-content: space-between;
          align-items: flex-start;
        "
        horizontal
      >
        <q-card-section
          class="col-7 flex q-pt-xs"
          style="align-content: flex-start; flex-direction: column"
        >
          <div class="text-caption">
            <q-chip
              clickable
              size="sm"
              square
              icon="folder"
              @click="$router.push(`/news/category/${i.category.id}/all-posts`)"
              :label="i.category.name"
            />
          </div>
          <div class="q-mt-sm q-mb-xs">
            <router-link
              class="text-subtitle2 title text-dark"
              :to="'/news/category/' + i.category_id + '/post/' + i.id"
              >{{ i.title }}</router-link
            >
          </div>
        </q-card-section>

        <q-card-section class="col-5 flex flex-center">
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
</template>

<script setup>
import { date } from "quasar";
import { wordNum } from "src/helpers/word";

const props = defineProps({
  posts: { type: Array },
  limit: { type: Number },
  count: { type: Number },
  load: { type: Boolean },
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
