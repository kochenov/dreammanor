<template>
  <q-dialog
    v-model="newsStore.open_add_news"
    persistent
    :maximized="maximizedToggle"
    transition-show="slide-up"
    transition-hide="slide-down"
  >
    <q-card class="">
      <q-bar>
        <div class="text-subtitle2">Добавить новость</div>
        <q-space />

        <q-btn
          dense
          flat
          icon="minimize"
          @click="maximizedToggle = false"
          :disable="!maximizedToggle"
        >
          <q-tooltip v-if="maximizedToggle" class="bg-white text-primary"
            >Minimize</q-tooltip
          >
        </q-btn>
        <q-btn
          dense
          flat
          icon="crop_square"
          @click="maximizedToggle = true"
          :disable="maximizedToggle"
        >
          <q-tooltip v-if="!maximizedToggle" class="bg-white text-primary"
            >Maximize</q-tooltip
          >
        </q-btn>
        <q-btn dense flat icon="close" v-close-popup>
          <q-tooltip class="bg-white text-primary">Close</q-tooltip>
        </q-btn>
      </q-bar>

      <q-card-section class="q-mt-xl q-pt-none flex flex-center">
        <div class="q-pa-md">
          <q-form @submit.prevent="onSubmit" class="q-gutter-md row">
            <q-input
              filled
              v-model="title"
              label="Заголовок"
              hint="Новостной заголовок"
              lazy-rules
              class="col-12"
              :rules="[
                (val) => (val && val.length > 0) || 'Please type something',
              ]"
            />

            <q-input
              filled
              v-model="sub_title"
              label="Второй заголовок"
              lazy-rules
              class="col-12"
              :rules="[
                (val) => (val && val.length > 0) || 'Please type something',
              ]"
            />
            <div class="row col-12 q-gutter-xs">
              <q-select
                class="col-11"
                filled
                @focus="updateCategory"
                v-model="category_id"
                :options="options"
                label="Категории"
              />
              <q-btn
                icon="add"
                class="col"
                size="md"
                square
                color="primary"
                @click="newsStore.open_add_news_category = true"
              />
            </div>
            <q-input
              filled
              v-model="short_description"
              label="Описание"
              lazy-rules
              class="col-12"
              :rules="[
                (val) => (val && val.length > 0) || 'Please type something',
              ]"
            />

            <q-editor v-model="content" class="col-12" min-height="5rem" />

            <div>
              <q-btn label="Submit" type="submit" color="primary" />
            </div>
          </q-form>
        </div>
      </q-card-section>
    </q-card>
  </q-dialog>
  <add-category @updateCategory="updateCategory" />
</template>

<script setup>
import { ref, onUpdated, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useNewsStore } from "../../store";
import { defineAsyncComponent } from "vue";

const AddCategory = defineAsyncComponent(() =>
  import("src/modules/news/components/admin/newCategory.vue")
);
const newsStore = useNewsStore();
const maximizedToggle = ref(true);

const router = useRouter();

const title = ref("");
const sub_title = ref("");
const category_id = ref("");
const short_description = ref("");
const content = ref("");

const options = ref([]);
const updateCategory = async () => {
  options.value = [];
  await newsStore.loadCategories();
  if (newsStore.categories[0]) {
    let mapOptions = newsStore.categories;
    mapOptions.forEach((i) => {
      options.value.push({
        id: i.id,
        label: i.name,
      });
    });
  }
};

onUpdated(async () => {
  title.value = "";
  category_id.value = "";
  short_description.value = "";
  content.value = "";
});

const onSubmit = async () => {
  let data = {
    title: title.value,
    category_id: category_id.value.id,
    short_description: short_description.value,
    content: content.value,
  };
  let res = await newsStore.addNewPost(data);
  if (res) {
    title.value = null;
    category_id.value = null;
    short_description.value = null;
    content.value = null;
    await newsStore.loadPosts();
    newsStore.open_add_news = false;
    router.push("/news/posts/all-posts");
  }
};
</script>

<style lang="scss" scoped></style>
