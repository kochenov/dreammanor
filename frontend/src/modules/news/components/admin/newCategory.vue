<template>
  <q-dialog
    v-model="newsStore.open_add_news_category"
    persistent
    :maximized="false"
    transition-show="slide-up"
    transition-hide="slide-down"
  >
    <q-card class="">
      <q-bar>
        <div class="text-subtitle2">Добавить новую категорию новостей</div>
        <q-space />

        <q-btn dense flat icon="close" v-close-popup>
          <q-tooltip class="bg-white text-primary">Закрыть</q-tooltip>
        </q-btn>
      </q-bar>

      <q-card-section class="q-mt-xl q-pt-none flex flex-center">
        <div class="q-pa-md">
          <q-form @submit.prevent="onSubmit" class="q-gutter-md row">
            <q-input
              filled
              v-model="name"
              label="Название"
              hint="Название для новой категории"
              lazy-rules
              class="col-12"
              :rules="[
                (val) => (val && val.length > 0) || 'Please type something',
              ]"
            />

            <div>
              <q-btn label="Добавить" type="submit" color="primary" />
            </div>
          </q-form>
        </div>
      </q-card-section>
    </q-card>
  </q-dialog>
</template>

<script setup>
import { ref } from "vue";
import { useNewsStore } from "../../store";

const newsStore = useNewsStore();

const name = ref("");

const emit = defineEmits(["updateCategory"]);

const onSubmit = async () => {
  let data = {
    name: name.value,
  };
  let res = await newsStore.addNewCategory(data);
  if (res) {
    name.value = "";
    emit("updateCategory");
    newsStore.open_add_news_category = false;
    //router.push("/news/posts/all-posts");
  }
};
</script>

<style lang="scss" scoped></style>
