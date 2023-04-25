<template>
  <q-item-section class="start" style="flex: 1 0 auto">
    <div class="flex justify-end">
      <q-btn color="secondary" padding="xs" class="lt-md" icon="menu_open">
        <q-menu :offset="[-2, 10]">
          <q-list style="min-width: 200px">
            <q-item
              v-for="item in component_lists"
              :key="item.to"
              :to="item.to"
              clickable
              v-close-popup
            >
              <q-item-section>{{ item.text_btn }}</q-item-section>
            </q-item>
          </q-list>
        </q-menu>
      </q-btn>
      <div class="q-pa-md q-gutter-sm gt-sm">
        <q-btn
          v-for="item in component_lists"
          :key="item.to"
          :to="item.to"
          color="secondary"
          square
          :outline="
            $route.params.id_component === item.name_component.toLowerCase()
              ? false
              : true
          "
          size="sm"
          :label="item.text_btn"
        />
      </div>
    </div>
  </q-item-section>
</template>

<script setup>
const props = defineProps({
  component_lists: {
    type: Array,
    default() {
      return [];
    },
  },
});
</script>

<style lang="scss" scoped></style>
