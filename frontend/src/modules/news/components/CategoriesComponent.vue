<template>
  <div class="q-pa-md my-grid">
    <q-card v-for="i in newsStore.categories" :key="i.id" class="my-card">
      <q-card-section class="bg-primary text-white">
        <div class="text-subtitle2">Категория</div>
        <div class="text-h6">{{ i.name }}</div>
      </q-card-section>

      <q-separator />

      <q-card-actions align="center">
        <q-btn
          dense
          color="primary"
          :to="`/news/category/${i.id}/all-posts`"
          outline
          icon-right="arrow_right_alt"
        />
      </q-card-actions>
    </q-card>
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { useNewsStore } from "../store";
const newsStore = useNewsStore();

onMounted(async () => {
  await newsStore.loadCategories();
});
</script>

<style lang="scss" scoped>
.my-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, 250px);
  gap: 40px;
}
</style>
