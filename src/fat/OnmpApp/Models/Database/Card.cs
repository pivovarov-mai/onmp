using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using SQLite;

namespace OnmpApp.Models.Database;

// Возможные типы медицинских карт
public enum CardStatus
{
    [Description("Черновик")]
    Draft,
    [Description("Готовый")]
    Ready,
    [Description("Шаблон")]
    Template,
    [Description("Архив")]
    Archive
}

// Короткое описание медицинской карты
[Table("Сards")]
public class Card
{

    [PrimaryKey, AutoIncrement]
    public int Id { get; set; }

    [NotNull, Indexed(Name = "userid_idx", Order = 1)]
    public int UserId { get; set; }

    [NotNull, MaxLength(64), Indexed(Name = "name_idx", Order = 1)]
    public string LowerName { get; set; }

    // Название карты 
    [NotNull, MaxLength(64)]
    public string Name { get; set; }

    // Дата вызова
    [NotNull]
    public DateTime Date { get; set; } = DateTime.Now;

    // Номер наряда
    [NotNull, MaxLength(64)]
    public string Order { get; set; }

    [NotNull, Indexed(Name = "status_idx", Order = 1)]
    public CardStatus Status { get; set; }

    // Комментарий 
    [MaxLength(64)]
    public string Comment { get; set; }
}

