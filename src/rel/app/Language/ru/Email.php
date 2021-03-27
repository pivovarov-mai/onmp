<?php
/**
 * Email language strings.
 *
 * @package    CodeIgniter
 * @author     CodeIgniter Dev Team
 * @copyright  2014-2019 British Columbia Institute of Technology (https://bcit.ca/)
 * @license    https://opensource.org/licenses/MIT	MIT License
 * @link       https://codeigniter.com
 * @since      Version 3.0.0
 * @filesource
 *
 * @codeCoverageIgnore
 */

return [
    'mustBeArray'          => 'В метод проверки эллектронной почты должен быть передан массив.',
    'invalidAddress'       => 'Неверная эллектронная почта: {0}',
    'attachmentMissing'    => 'Невозможно найти следующее вложение электронной почты: {0}',
    'attachmentUnreadable' => 'Невозможно открыть это вложение: {0}',
    'noFrom'               => 'Невозможно отправить письмо без заголовка «От»..',
    'noRecipients'         => 'Вы должны включить получателей: Кому, Копия или Скрытая копияc',
    'sendFailurePHPMail'   => 'Невозможно отправить письмо используя PHP mail(). Возможно, ваш сервер не настроен на отправку почты с использованием этого метода.',
    'sendFailureSendmail'  => 'Невозможно отправить письмо с помощью PHP Sendmail. Возможно, ваш сервер не настроен на отправку почты с использованием этого метода.',
    'sendFailureSmtp'      => 'Невозможно отправить письмо, используя PHP SMTP. Возможно, ваш сервер не настроен на отправку почты с использованием этого метода.',
    'sent'                 => 'Ваше сообщение было успешно отправлено по следующему протоколу: {0, string}',
    'noSocket'             => 'Невозможно открыть сокет для Sendmail. Пожалуйста, проверьте настройки.',
    'noHostname'           => 'Вы не указали имя хоста SMTP.',
    'SMTPError'            => 'Обнаружена следующая ошибка SMTP: {0}',
    'noSMTPAuth'           => 'Ошибка: необходимо назначить имя пользователя и пароль SMTP.',
    'failedSMTPLogin'      => 'Не удалось отправить команду AUTH LOGIN. Ошибка: {0}',
    'SMTPAuthUsername'     => 'Не удалось аутентифицировать имя пользователя. Ошибка: {0}',
    'SMTPAuthPassword'     => 'Не удалось подтвердить пароль. Ошибка: {0}',
    'SMTPDataFailure'      => 'Невозможно отправить данные: {0}',
    'exitStatus'           => 'Код состояния выхода: {0}',
];