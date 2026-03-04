<?php

namespace App\Http\Controllers;

class OrderController extends Controller
{
    public function index()
    {
        return response()->json([
            'message' => 'Order list mock endpoint',
        ]);
    }
}
