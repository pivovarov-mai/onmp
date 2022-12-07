using SQLite;

namespace OnmpApp.Models;

[Table("Users")]
public class User
{
    [PrimaryKey, AutoIncrement]
    public int Id { get; set; }
    [NotNull, Indexed(Name = "email_idx", Order = 1, Unique = true)]
    public string Email { get; set; }
    [NotNull]
    // TODO: сделать шифрование для пароля
    public string Password { get; set; }
    [NotNull]
    public DepartmentType DepartmentType { get; set; } = 0;

    public User() { }
    public User(string email, string password, DepartmentType departmentType = 0)
    {
        Email = email;
        Password = password;
        DepartmentType = departmentType;
    }
}

public enum DepartmentType
{
    ОНМП,
    СНП
}
