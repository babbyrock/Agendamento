import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AccountService } from 'src/app/services/Account/account.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  constructor(public accountService: AccountService,
              private router: Router) { }

  ngOnInit(): void {
  }


  logout(): void {
    this.accountService.logout();
    this.router.navigateByUrl('/login');
  }
}
