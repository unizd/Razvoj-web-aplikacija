import { NgModule } from  '@angular/core';
import { Routes, RouterModule } from  '@angular/router';

import { AdminComponent } from  './admin/admin.component';
import { AdminListComponent } from  './admin-list/admin-list.component';

const  routes:  Routes  = [
{
path:  'admin',
component:  AdminComponent,
children: [
{
path:  'list',
component:  AdminListComponent
},
]
}
];
@NgModule({
imports: [RouterModule.forChild(routes)],
exports: [RouterModule]
})
export  class  AdminRoutingModule { }
