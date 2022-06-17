# Підключення бібліотеки для роботи з БД
import sqlite3

class BotDB:

    def __init__(self, db_file):
        """Підключення до бази данних"""
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        """Перевірка чи є користувач у базі данних"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_user_id(self, user_id):
        """Дістаємо id юзера в базі по його user_id"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()[0]

    def add_user(self, user_id):
        """Добавляємо юзера в базу данних"""
        self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
        return self.conn.commit()

    def add_record(self, user_id, name, notise, value):
        """Створюємо запис по витратах"""
        self.cursor.execute("INSERT INTO `records` (`users_id`, `name`, `notise`, `value`) VALUES (?, ?, ?, ?)",
            (self.get_user_id(user_id),name, notise, value))
        return self.conn.commit()

    def get_records(self, user_id, within = "all"):
        """Отримуємо історію по витратах"""

        if(within == "day"):
            """Отримуємо історію по витратах за день"""
            result = self.cursor.execute("SELECT * FROM `records` WHERE `users_id` = ? AND `date` BETWEEN datetime('now', 'start of day') AND datetime('now', 'localtime') ORDER BY `date`",
                (self.get_user_id(user_id),))
        elif(within == "week"):
            """Отримуємо історію по витратах за тиждень"""
            result = self.cursor.execute("SELECT * FROM `records` WHERE `users_id` = ? AND `date` BETWEEN datetime('now', '-6 days') AND datetime('now', 'localtime') ORDER BY `date`",
                (self.get_user_id(user_id),))
        elif(within == "month"):
            """Отримуємо історію по витратах за місяць"""
            result = self.cursor.execute("SELECT * FROM `records` WHERE `users_id` = ? AND `date` BETWEEN datetime('now', 'start of month') AND datetime('now', 'localtime') ORDER BY `date`",
                (self.get_user_id(user_id),))
        elif(within == "year"):
            """Отримуємо історію по витратах за рік"""
            result = self.cursor.execute("SELECT * FROM `records` WHERE `users_id` = ? AND `date` BETWEEN datetime('now', 'start of year') AND datetime('now', 'localtime') ORDER BY `date`",
                (self.get_user_id(user_id),))
        elif(within == "all"):
            """Отримуємо історію по витратах за весь час"""
            result = self.cursor.execute("SELECT * FROM `records` WHERE `users_id` = ? ORDER BY `date`",
                (self.get_user_id(user_id),))
        else:
            """Отримуємо історію по витратах за весь час"""
            result = self.cursor.execute("SELECT * FROM `records` WHERE `users_id` = ? ORDER BY `date`",
                (self.get_user_id(user_id),))

        return result.fetchall()

    def close(self):
        """Закриваєм з'єднання з базою данних"""
        self.connection.close()