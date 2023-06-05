using SQLite;

namespace OnmpApp.Models.Database;

[Table("Users")]
public class User
{
    [PrimaryKey, AutoIncrement]
    public int Id { get; set; }
    [NotNull, Indexed(Name = "email_idx", Order = 1, Unique = true)]
    public string Email { get; set; }
    public User() { }
    public User(string email)
    {
        Email = email;
    }
}
