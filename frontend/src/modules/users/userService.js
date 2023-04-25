export default {
  /**
   * Add database new user
   * @param {*} uid ID user
   * @param {*} payload {email, name, online}
   */
  createUser(uid, payload) {
    return set(ref(db, "users/" + uid), {
      name: payload.name,
      email: payload.email,
      online: true,
    });
  },
  /**
   * Получение текущего пользователя с Ferebase
   * @param {*} uid Уникальный идентификатор пользователя
   * @returns Промис
   */
  async getCurrentUser(uid) {
    const dbRef = ref(db);
    return await get(child(dbRef, `users/${uid}`));
  },
  /**
   * Получение списка пользователей
   * @returns промис
   */
  async getAllUsers() {
    const dbRef = ref(db);
    return await get(child(dbRef, `users`));
  },
};
