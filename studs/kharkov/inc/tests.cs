public class UserServiceTests
{
    [Theory]
    [InlineData("", "")]
    [InlineData("ads@akd@", "p")]
    [InlineData("wrong@email.ru", "pass")]
    // Тестирование аутентификации с неверными данными пользователей
    public async Task AuthenticateUser_False(string email, string password)
    {
        Assert.False(await UserService.Authenticate(email, password));
    }
    [Theory]
    [InlineData("a@b.c", "abc")]
    [InlineData("k.p.a@m.ru", "1#121")]
    [InlineData("LongMail@yandex.ru", "1Long##Pass")]
    // Тестирование аутентификации с верными данными уже созданных пользователей
    public async Task AuthenticateUser_True(string email, string password)
    {
        Assert.True(await UserService.Authenticate(email, password));
    }
}