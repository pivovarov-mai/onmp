using OnmpApp.Models;
using System.ComponentModel;
using System.Reflection;
using System.Text.RegularExpressions;
using OnmpApp.Models.Database;

namespace OnmpApp.Helpers;

public static class StringHelper
{
    // Проверка строки, является ли она почтой
    public static bool IsEmail(this string str)
    {
        if (string.IsNullOrEmpty(str))
            return false;
        string pattern = "^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$";
        return Regex.IsMatch(str.ToLower(), pattern);
    }

    // Получение описания поля
    public static string GetDescription(this Enum value)
    {
        FieldInfo field = value.GetType().GetField(value.ToString());
        DescriptionAttribute attribute = field.GetCustomAttribute<DescriptionAttribute>();
        return attribute == null ? value.ToString() : attribute.Description;
    }

    public static CardStatus GetEnumFromDescription(string description)
    {
        return description switch
        {
            "Черновик" => CardStatus.Draft,
            "Готовый" => CardStatus.Ready,
            "Шаблон" => CardStatus.Template,
            "Архив" => CardStatus.Archive,
            _ => throw new ArgumentException("Не найдено соответствующее значение для описания.")
        };
    }
}
