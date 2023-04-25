<template>
  <div class="row-grid" v-if="items">
    <q-card class="my-card column" v-for="i in items" :key="i.id">
      <q-img style="height: 210px;" :src="`https://api.dreammanor.ru/${i.main_image}`"> </q-img>
      <q-card-section class="q-pb-none">
        <q-chip square icon="location_on" size="11px"
          >{{ i.region.label }}
        </q-chip>
        <q-chip square icon="directions" size="11px"
          >{{ i.district.label }}
        </q-chip>
      </q-card-section>
      <q-card-section class="q-pt-md">
        <q-list dense>
          <q-item>
            <q-item-section>
              <q-item-label>Цена</q-item-label>
            </q-item-section>

            <q-item-section side top>
              <q-item-label caption>
                <q-icon name="currency_ruble" size="32px" />
                <span class="text-grey-14">{{ i.price }}</span></q-item-label
              >
            </q-item-section>
          </q-item>

          <q-item>
            <q-item-section>
              <q-item-label>Дом</q-item-label>
            </q-item-section>

            <q-item-section side top>
              <q-item-label caption>
                <q-chip square dense color="secondary" text-color="white">
                  {{ i.area_of_house }} кв.м
                </q-chip>
              </q-item-label>
            </q-item-section>
          </q-item>

          <q-item>
            <q-item-section>
              <q-item-label>Участок</q-item-label>
            </q-item-section>

            <q-item-section side top>
              <q-item-label caption>
                <q-chip square dense color="secondary" text-color="white">
                  25 соток
                </q-chip>
              </q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-card-section>

      <q-separator class="q-mt-auto" />

      <q-card-actions class="">
        <q-btn flat round color="primary" class="custom-btn">
          <q-icon name="favorite_border" :color="'grey'" />
        </q-btn>
        <q-space />
        <q-rating
          :model-value="3"
          readonly
          max="5"
          size="1.8em"
          color="yellow"
          icon="star_border"
          icon-selected="star"
          icon-half="star_half"
          no-dimming
        />
        <q-space />
        <q-btn flat :to="`/desk/realEstate/home/${i.id}`" color="primary">
          Подробнее
        </q-btn>
      </q-card-actions>
    </q-card>
  </div>
  <div v-else>
    <div class="q-pa-md flex flex-center q-gutter-sm">
      <q-banner style="max-width: 650px" class="text-white bg-info">
        Нет опубликованных объявлений.
        <template v-slot:action>
          <q-btn
            flat
            to="/desk/realEstate/links/add-new-ads-home"
            color="white"
            label="Создать объявление сейчас"
          />
        </template>
      </q-banner>
    </div>
  </div>
</template>

<script setup>
const props = defineProps(["items"]);
</script>

<style lang="scss" scoped>
.row-grid {
  display: grid;

  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  @media (max-width: $breakpoint-sm-max) {
    grid-template-columns: repeat(auto-fit, minmax(270px, 1fr));
  }
  gap: 30px;
  justify-content: center;
}
.custom-btn:hover .q-icon {
  color: red !important;
}
</style>
