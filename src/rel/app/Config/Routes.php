<?php namespace Config;

// Create a new instance of our RouteCollection class.
$routes = Services::routes();

// Load the system's routing file first, so that the app and ENVIRONMENT
// can override as needed.
if (file_exists(SYSTEMPATH . 'Config/Routes.php'))
{
	require SYSTEMPATH . 'Config/Routes.php';
}

/**
 * --------------------------------------------------------------------
 * Router Setup
 * --------------------------------------------------------------------
 */
$routes->setDefaultNamespace('App\Controllers');
$routes->setDefaultController('Login');
$routes->setDefaultMethod('index');
$routes->setTranslateURIDashes(false);
$routes->set404Override(function () {
	echo view('templates/html_header');
	echo view('errors/html/error_404');
	echo view('templates/html_footer');
});
$routes->setAutoRoute(false);

/**
 * --------------------------------------------------------------------
 * Route Definitions
 * --------------------------------------------------------------------
 */

// We get a performance increase by specifying the default
// route since we don't have to scan directories.
$routes->add('/', 'Card::index', ['filter' => 'auth']);
$routes->get('/about', 'About::index');
$routes->get('/test', 'Login::sendmail');

$routes-> get('/login', 'Login::enter_form');
$routes->post('/auth', 'Login::auth');
$routes-> get('/block', 'Login::block');
$routes-> get('/forget_password', 'Login::request_password_form');
$routes->post('/request_password', 'Login::new_password_request');
$routes-> get('/verify/(:any)', 'Register::new_password_form/$1'); 
$routes->post('/update_password/(:any)', 'Register::update_password/$1');
$routes-> get('/exit', 'Login::logout');
$routes->post('/feedback', 'Login::sendmail');
//$routes-> get('/test_mail', 'Login::sendmail');

// AJAX modification/selection DB
$routes->post('/update', 'Card::update', ['filter' => 'auth']);
$routes->post('/delete/(:num)', 'Card::delete/$1', ['filter' => 'auth']);
$routes->post('/create', 'Card::create', ['filter' => 'auth']);

$routes-> get('/registration', 'Register::add_email_form');
$routes->post('/register', 'Register::register_email');
$routes-> get('/verify/(:any)', 'Register::new_password_form/$1'); 

// AJAX request for client
$routes->post('/(draft|ready|template|archive)', 'Card::list/$1', ['filter' => 'auth']);
$routes-> get('/download/(:num)/(:any)', 'Card::download/$1/$2', ['filter' => 'auth']);
$routes->post('/card/(:num)', 'Card::json/$1', ['filter' => 'auth']);

$routes->get('/table', 'Table::index');
// or such
// $routes->addPlaceholder('status', 'draft|ready|template|archive');
// $routes->post('/(:status)', 'Card::list/$1');



/**
 * --------------------------------------------------------------------
 * Additional Routing
 * --------------------------------------------------------------------
 *
 * There will often be times that you need additional routing and you
 * need it to be able to override any defaults in this file. Environment
 * based routes is one such time. require() additional route files here
 * to make that happen.
 *
 * You will have access to the $routes object within that file without
 * needing to reload it.
 */
if (file_exists(APPPATH . 'Config/' . ENVIRONMENT . '/Routes.php'))
{
	require APPPATH . 'Config/' . ENVIRONMENT . '/Routes.php';
}
